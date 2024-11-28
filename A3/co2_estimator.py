import ifcopenshell
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm 
import json
import numpy as np
import ifcopenshell
from pathlib import Path

class ModelWithEstimator:
    def __init__(self, dir_path, arc_path, str_path, mep_path):
        """
        Initialize the IFCModelHandler with paths to architectural, structural, and MEP models.
        
        Args:
            dir_path (str): The base directory path where the IFC files are located.
            arc_path (str): The filename of the architectural model.
            str_path (str): The filename of the structural model.
            mep_path (str): The filename of the MEP model.
        """
        self.dir_path = dir_path
        self.arc_path = Path(self.dir_path + arc_path)
        self.str_path = Path(self.dir_path + str_path)
        self.mep_path = Path(self.dir_path + mep_path)

        self._validate_paths()

        self.arc_model = ifcopenshell.open(self.arc_path)
        self.str_model = ifcopenshell.open(self.str_path)
        self.mep_model = ifcopenshell.open(self.mep_path)

    def _validate_paths(self):
        """
        Validate that all specified paths exist as files.
        """
        for model_path in [self.arc_path, self.str_path, self.mep_path]:
            if not model_path.is_file():
                raise FileNotFoundError(f"No file found at {model_path}!")

    def get_models(self):
        """
        Return the loaded models as a dictionary.
        
        Returns:
            dict: A dictionary containing the loaded models.
        """
        return {
            'Architectural': self.arc_model,
            'Structural': self.str_model,
            'MEP': self.mep_model
        }
    
    @staticmethod
    def simplify_name(name):
        return ":".join(name.split(":")[:2]) if ":" in name else name

    @staticmethod
    def clean_materials(materials):
        filtered_materials = [mat for mat in materials if mat and mat.lower() != "unknown"]
        return list(set(filtered_materials)) if filtered_materials else ["Unknown"]

    @staticmethod
    def scale_quantities(quantities, unit_definitions):
        scaled_quantities = {}
        for key, value in quantities.items():
            if key == "Length" and unit_definitions.get("LENGTHUNIT") == ("MILLI", "METRE"):
                scaled_quantities[key] = value / 1000
            elif key == "Area" and unit_definitions.get("AREAUNIT") == ("", "SQUARE_METRE"):
                scaled_quantities[key] = value
            elif key == "Volume" and unit_definitions.get("VOLUMEUNIT") == ("", "CUBIC_METRE"):
                scaled_quantities[key] = value
            else:
                scaled_quantities[key] = value
        return scaled_quantities

    @staticmethod
    def clean_material_text(materials_list):
        material_categories = {
            "Concrete": ["Concrete", "Cast-in-Place", "Precast"],
            "Steel": ["Steel", "Galvanized", "Polished"],
            "Wood": ["Wood", "Joist", "Rafter"],
            "Insulation": ["Insulation", "Rigid"],
            "Cladding": ["Clad"],
            "Glass": ["Glass", "Glazing"],
            "Tiles": ["Tile"],
            "Plaster": ["Plaster"],
            "Shingles": ["Shingle"]
        }

        def map_material(material):
            for category, keywords in material_categories.items():
                if any(keyword.lower() in material.lower() for keyword in keywords):
                    return category
            return material 

        cleaned_materials = []
        for raw_material in materials_list:
            split_materials = [mat.strip() for mat in raw_material.split(",")]

            standardized_materials = [map_material(mat) for mat in split_materials]
            unique_materials = sorted(set(standardized_materials))
            cleaned_materials.append(unique_materials)

        return cleaned_materials

    def extract_element_data(self, building_element_types):
        """
        Given input element_types and ifc models, extract name, quantity and material information of the elements

        Args:
            building_element_types (List(str)): List of desired element types

        
        Returns:
            Dataframe: A pandas dataframe containing the extracted information
        """
        element_data = {}
        models = [self.arc_model, self.str_model, self.mep_model]

        def get_unit_definitions(self):
            unit_definitions = {}
            for project in self.arc_model.by_type("IfcProject"):
                if project.UnitsInContext:
                    for unit in project.UnitsInContext.Units:
                        if unit.is_a("IfcSIUnit"):
                            unit_type = unit.UnitType  
                            unit_prefix = unit.Prefix or "" 
                            unit_name = unit.Name 
                            unit_definitions[unit_type] = (unit_prefix, unit_name)
            return unit_definitions
        
        unit_definitions = get_unit_definitions(self)

        for model in models:
            for element_type in building_element_types:
                elements = model.by_type(element_type)
                for element in elements:
                    materials = set()
                    quantities = {}

                    if hasattr(element, 'HasAssociations'):
                        for association in element.HasAssociations:
                            if association.is_a("IfcRelAssociatesMaterial"):
                                material = association.RelatingMaterial
                                if material:
                                    if material.is_a("IfcMaterialLayerSet"):
                                        for layer in material.MaterialLayers:
                                            if layer.Material:
                                                materials.add(layer.Material.Name)
                                    elif material.is_a("IfcMaterialProfileSet"):
                                        for profile in material.MaterialProfiles:
                                            if profile.Material:
                                                materials.add(profile.Material.Name)
                                    elif material.is_a("IfcMaterial"):
                                        materials.add(material.Name)

                    if hasattr(element, 'IsDefinedBy'):
                        for definition in element.IsDefinedBy:
                            if definition.is_a("IfcRelDefinesByProperties"):
                                properties = definition.RelatingPropertyDefinition
                                if properties.is_a("IfcPropertySet"):
                                    for prop in properties.HasProperties:
                                        if prop.Name == "Material" and prop.NominalValue:
                                            materials.add(prop.NominalValue.wrappedValue)

                    if hasattr(element, 'IsDefinedBy'):
                        for definition in element.IsDefinedBy:
                            if definition.is_a("IfcRelDefinesByProperties"):
                                properties = definition.RelatingPropertyDefinition
                                if properties.is_a("IfcPropertySet"):
                                    for prop in properties.HasProperties:
                                        if prop.Name in ["Area", "Volume", "Length"]:
                                            quantities[prop.Name] = prop.NominalValue.wrappedValue
                                elif properties.is_a("IfcElementQuantity"):
                                    for quantity in properties.Quantities:
                                        if quantity.is_a("IfcQuantityVolume"):
                                            quantities["Volume"] = quantity.VolumeValue
                                        elif quantity.is_a("IfcQuantityArea"):
                                            quantities["Area"] = quantity.AreaValue
                                        elif quantity.is_a("IfcQuantityLength"):
                                            quantities["Length"] = quantity.LengthValue

                    element_data[element.GlobalId] = {
                        "ElementType": element.is_a(),
                        "Name": self.simplify_name(element.Name),
                        "Materials": self.clean_materials(materials),
                        "Quantities": self.scale_quantities(quantities, unit_definitions) if quantities else {} 
                    }

        for element_id, data in element_data.items():
            raw_materials = data.get("Materials", [])
            cleaned_materials = self.clean_material_text([", ".join(raw_materials)])[0]
            element_data[element_id]["Materials"] = cleaned_materials

        self.df = pd.DataFrame([
            {
                "ElementName": data["ElementType"],
                "SubType": data["Name"],
                "Length": data["Quantities"].get("Length"),
                "Area": data["Quantities"].get("Area"),
                "Volume": data["Quantities"].get("Volume"),
                "Material": ", ".join(data["Materials"]) if data["Materials"] else None
            }
            for data in element_data.values()
        ])

        self.df = self.df[~((self.df['Volume'].isna()) & (self.df['Length'].isna()))]

        return self.df
    
    def impute_materials(self, material_data):
        """
        Impute records without material with assumed material
        """
        df_without_material = self.df[self.df['Material'].isin(['Unknown', '<Unnamed>'])]
        df_with_material = self.df[~self.df['Material'].isin(['Unknown', '<Unnamed>'])]
        
        material_df = pd.Series(material_data).reset_index()
        material_df.columns = ['SubType', 'Material']
        
        annotated_data = pd.merge(df_without_material, 
                                material_df, on='SubType', 
                                how='inner').drop('Material_x', axis=1)
        annotated_data.rename(columns={'Material_y': 'Material'}, inplace=True)
        
        self.df = pd.concat([df_with_material, annotated_data])
    
    def calculate_co2(self,co2_data):
        """
        Use two helper functions and external CO2 data, annotate datafram with
        CO2 values and calculate annual emissions per element. Prioritise using 
        volume to make calculations, if not available, fallback on area or length.
        """
        def annotate_with_co2(row, co2_data):
            material = row['Material']
            if pd.notna(row['Volume']):
                row['Co2'] = co2_data.get('CO2_per_volume', None)
            elif pd.notna(row['Area']):
                row['Co2'] = co2_data.get('CO2_per_area', None)
            else:
                row['Co2'] = co2_data.get('CO2_per_length', None)
            return row

        def calculate_element_co2(row):
            if pd.notna(row['Volume']):
                row['Annual_Co2'] = row['Volume']*row['Co2']
            elif pd.notna(row['Area']):
                row['Annual_Co2'] = row['Area']*row['Co2']
            else:
                row['Annual_Co2'] = row['Length']*row['Co2']
            return row
        
        df_with_co2 = self.df.apply(lambda row: annotate_with_co2(row, co2_data[row['Material']]), axis=1)
        self.df = df_with_co2.apply(calculate_element_co2, axis=1)

        return self.df

    def show_total_element_co2(self):
        """
        Show annual CO2 emission for all elements
        """
        total_element_co2 = self.df.groupby('ElementName')['Annual_Co2'].sum()
        total_element_co2 = total_element_co2.reset_index()
        print(total_element_co2)
        return total_element_co2

    def show_co2_for_element(self, element_name):
        """
        Show annual CO2 emission for the input element(s)
        
        Args:
            element_name (List(str)): List of desired elements
        """
        df_subset = self.df[self.df['ElementName'].isin(element_name)]
        selected_element_co2 = df_subset.groupby('ElementName')['Annual_Co2'].sum()
        selected_element_co2 = selected_element_co2.reset_index()
        print(selected_element_co2)
        return selected_element_co2

    def show_total_co2(self):
        """
        Show building's total annual CO2 emission
        """
        print(f"Total building's Annual CO2: {np.round(self.df['Annual_Co2'].sum())} kg")

    def plot_results(self):
        """
        Plots a pie chart to show each element's contribution to total CO2 emission
        Plots a bar chart to compare total CO2 emission per element
        """ 
        total_element_co2 = self.df.groupby('ElementName')['Annual_Co2'].sum()
        total_element_co2 = total_element_co2.reset_index()
        colors = cm.tab20c(range(len(total_element_co2['Annual_Co2'])))
        fig, axes = plt.subplots(2, 1, figsize=(10, 12))

        # Pie Chart
        total = total_element_co2['Annual_Co2'].sum()
        percentages = (total_element_co2['Annual_Co2'] / total) * 100
        legend_labels = [
            f"{name} ({value:.1f}%)"
            for name, value in zip(total_element_co2['ElementName'], percentages)
        ]
        wedges, _ = axes[0].pie(
            total_element_co2['Annual_Co2'], 
            labels=None, 
            colors=colors, 
            startangle=90
        )
        axes[0].legend(
            wedges, 
            legend_labels, 
            title="Element Types", 
            loc="best", 
            bbox_to_anchor=(1, 1), 
            fontsize='large'
        )
        axes[0].set_title('Share of Annual CO2 Emission By Element')

        # Bar Chart
        sorted_data = total_element_co2.sort_values(by='Annual_Co2', ascending=False)
        bars = axes[1].bar(
            sorted_data['ElementName'], 
            sorted_data['Annual_Co2'], 
            color=colors, 
            alpha=0.85,
            edgecolor='black'
        )
        for bar in bars:
            height = np.round(bar.get_height())
            axes[1].text(
                bar.get_x() + bar.get_width() / 2, 
                height, 
                height, 
                ha='center', 
                va='bottom', 
                rotation=90, 
                fontsize=9,
                color='darkblue',
                fontweight='bold'
            )
        axes[1].set_xticklabels(sorted_data['ElementName'], rotation=90, fontsize=9, ha='center')
        axes[1].set_ylabel('Annual CO2 Emissions', fontsize=12, labelpad=10)
        axes[1].set_title('Total Annual CO2 Emissions by Element')
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.gca().set_facecolor('#f4f4f8') 

        plt.tight_layout()
        plt.show()

    def generate_plots(self, directory=".", pie_filename="pie_chart.jpeg", bar_filename="bar_chart.jpeg"):
        """
        Saves the pie chart and bar chart as JPEG files.
        
        Parameters:
            directory (str): directory to save the images
            pie_filename (str): filename for the pie chart image.
            bar_filename (str): filename for the bar chart image.
        """
        total_element_co2 = self.df.groupby('ElementName')['Annual_Co2'].sum().reset_index()
        colors = cm.tab20c(range(len(total_element_co2['Annual_Co2'])))

        # Pie Chart
        plt.figure(figsize=(8, 6))
        total = total_element_co2['Annual_Co2'].sum()
        percentages = (total_element_co2['Annual_Co2'] / total) * 100
        legend_labels = [
            f"{name} ({value:.1f}%)"
            for name, value in zip(total_element_co2['ElementName'], percentages)
        ]
        wedges, _ = plt.pie(
            total_element_co2['Annual_Co2'], 
            labels=None, 
            colors=colors, 
            startangle=90
        )
        plt.legend(
            wedges, 
            legend_labels, 
            title="Element Types", 
            loc="best", 
            bbox_to_anchor=(1, 1), 
            fontsize='large'
        )
        plt.title('Share of Annual CO2 Emission By Element')
        plt.tight_layout()
        pie_path = Path(directory) / pie_filename
        plt.savefig(pie_path, format="jpeg")
        plt.close() 

        # Bar Chart
        plt.figure(figsize=(10, 6))
        sorted_data = total_element_co2.sort_values(by='Annual_Co2', ascending=False)
        bars = plt.bar(
            sorted_data['ElementName'], 
            sorted_data['Annual_Co2'], 
            color=colors, 
            alpha=0.85,  
            edgecolor='black'
        )

        for bar in bars:
            height = np.round(bar.get_height())
            plt.text(
                bar.get_x() + bar.get_width() / 2, 
                height, 
                height, 
                ha='center', 
                va='bottom', 
                rotation=90, 
                fontsize=9, 
                color='darkblue',  
                fontweight='bold' 
            )

        plt.xticks(
            sorted_data['ElementName'], 
            rotation=90, 
            fontsize=9, 
            ha='center'
        )

        plt.ylabel('Annual CO2 Emissions', fontsize=12, labelpad=10)
        plt.title('Total Annual CO2 Emissions by Element', fontsize=14, pad=15)
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.gca().set_facecolor('#f4f4f8') 
        plt.tight_layout()
        bar_path = Path(directory) / bar_filename
        plt.savefig(bar_path, format="jpeg")
        plt.close()

        print(f"Plots saved: \n- Pie Chart: {pie_path}\n- Bar Chart: {bar_path}")
  
        



