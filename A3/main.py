from co2_estimator import ModelWithEstimator
import json
from pathlib import Path

def calculate_results():
    script_dir = Path(__file__).parent.resolve()
    dir_path = "C:/Users/romin/Desktop/Advanced Bilding information modelling/CES_BLD_24_06_"
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
    #results.generate_plots()
    results.plot_results()

