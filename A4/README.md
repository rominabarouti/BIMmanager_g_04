
# Role Identification and Learning Progress 
In this project, we took on the role of BIM managers, focusing on architecture as the primary discipline. Our responsibilities included managing workflows, facilitating collaboration between disciplines, and utilizing BIM tools. Initially, our understanding of BIM was at a beginner level, but throughout the lectures and exercises, we progressed to an intermediate level. This role required us to develop problem-solving skills, enhance our technical expertise, and effectively communicate to achieve project objectives.

# BIM uses: Sustainability Analysis 
We chose **Sustainability Analysis** as our focus area, specifically to evaluate the CO₂ emissions of the materials and elements used in the model. Sustainability analysis in BIM involves assessing a building's environmental performance across its lifecycle, from planning and design to construction and operation. This process typically utilizes frameworks like LEED or Green Globes to integrate sustainable features early in the project, emphasizing collaboration across disciplines to achieve cost-effective and environmentally impactful designs.
Our specific use case focused on quantifying the CO₂ emissions of building elements and materials. By analyzing the elements in the model, we aimed to understand their environmental impact, enabling informed decisions about material selection and design alternatives. This approach required extracting and organizing detailed data from IFC models, assigning material properties, and using calculation standards like EN15978. The use of python and ifcopenshell library, sustainability metrics, and data management capabilities was critical to achieving these goals.

# CO₂ Emission Analysis with BIM Models
**Summary:** We extracted building elements from IFC models, assigned assumed materials, and calculated CO₂ emissions using Python. The results were visualized to highlight environmental impacts and identify opportunities for improvement.

# Summary

**Title:** Using Python and Ifcopenshell to estimate building's CO2 emission

**Description:**  A python tool that takes advantage of ifcopenshell library to extract element quantity and material information and combines it with external CO2 emission factors to calculate annual CO2 footprint of building elements. The tool also provides plots for better assessment of the results.

# Code Snippets

Here are a few snippets of the tool to demonstrate how the tool was created. For a visual walkthrough, click on this [link](https://youtu.be/JVlfLT0Y1Ok). The tool is a python class with several methods to calculate and display results. 

### Class Definition and Construction

```
class ModelWithEstimator:
    def __init__(self, dir_path, arc_path, str_path, mep_path):
        self.dir_path = dir_path
        self.arc_path = Path(self.dir_path + arc_path)
        self.str_path = Path(self.dir_path + str_path)
        self.mep_path = Path(self.dir_path + mep_path)

        self._validate_paths()

        self.arc_model = ifcopenshell.open(self.arc_path)
        self.str_model = ifcopenshell.open(self.str_path)
        self.mep_model = ifcopenshell.open(self.mep_path)
```

### Information Extraction from IFC Models (partial code)

```
def extract_element_data(self, building_element_types):
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

```

### Get Total CO2 Per IFC Element

```
def show_total_element_co2(self):
    total_element_co2 = self.df.groupby('ElementName')['Annual_Co2'].sum()
    total_element_co2 = total_element_co2.reset_index()
    print(total_element_co2)
    return total_element_co2
```

### Tool Usage

```
def calculate_results():
    script_dir = Path(__file__).parent.resolve()
    dir_path = "DIRECTORY_PATH_TO_FILES"
    arc_path = "ARC.ifc"
    str_path = "STR.ifc"
    mep_path = "MEP.ifc"

    model = ModelWithEstimator(dir_path, arc_path, str_path, mep_path)
    building_element_types = [
    "IfcWall", "IfcSlab", "IfcColumn", "IfcBeam", "IfcDoor", "IfcWindow",
    "IfcStair", "IfcRoof", "IfcCovering", "IfcCurtainWall",
    "IfcFlowSegment", "IfcPipeSegment", "IfcPipeFitting",
    "IfcDuctSegment", "IfcDuctFitting", "IfcFan", "IfcFlowTerminal"
    ]

    model.extract_element_data(building_element_types)
    material_path = script_dir / "assumed_materials.json"
    with open(material_path, 'r') as file:
        assumed = json.load(file)

    model.impute_materials(assumed)

    co2_path = script_dir / "co2_data.json"
    with open(co2_path, 'r') as co2_file:
        co2_data = json.load(co2_file)

    model.calculate_co2(co2_data)

    return model


if __name__ == '__main__':
    results = calculate_results()
    results.show_total_element_co2()
    results.show_total_co2()
    results.show_co2_for_element(['IfcBeam'])
    results.plot_results()

```


# Feedback 

## Group 8: Tool for optimization of space for each emplyees

#### Space management: how to obtain optimum space organization 
**Challenges:** Information required for calculation floor area is missing. Finding floor numbers, slab types, and identifying furnitures were also challenging.

**Solution:** Use BIMVision which is a better solution than BlenderBIM. 


## Group 2: Tool to check fire escape stairs and routes  


**Challenges and Solutions:** Stairs did not have properties so the global coordinates of stairs were used and grouped together instead. 
The group was determined to update the model since most properties were missing. Additionally, ceiling height was not the same as stair heights. 


## Group 9:  Tool to find fire safety codes for buildings 

#### Fire safety codes help engineers find out which type of walls, stairs, etc is needed for fire safety.

**Challenges and solutions:** It was challenging to find ground floor to top height as they could only retrieve basement to top height. The obtained height unit was in milimeters whereas they needed them in meters for which they tried finding a function to change to the desired unit. Requirements in Danish or other languages were hard to find. If there were a global standard for the requirements, the tool could have been made universal.