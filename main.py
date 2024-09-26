import ifcopenshell
from external.Group1.Heightfloor2floorRule import checkRule
from external.Group9.rules.wallRule import calculate_wall_area

model_path = "C:/Users/romin/Desktop/Advanced Bilding information modelling/CES_BLD_24_06_ARC.ifc"
model = ifcopenshell.open(model_path)


# Group 1 

print("---------Group 1 Results-----------")
checkRule(model) # Calculates and prints Floor2floor heights

roofs = model.by_type('Ifcroof')
print("Number of roofs", len(roofs))

elevations = model.by_type('IfcBuildingStorey')
print("Number of elevations", len(elevations))

# Group 6
print("---------Group 6 Results-----------")
windows = model.by_type('IfcWindow')
print("Number of windows", len(windows))

plates = model.by_type('IfcPlate')
print("Number of plates", len(plates))

curtain_walls = model.by_type('IfcCurtainWall')
print("Number of curtain walls", len(curtain_walls))

# Group 8
print("---------Group 8 Results-----------")
doors = model.by_type('IfcDoor')
print("Number of doors",len(doors))

door_types = model.by_type('IfcDoorType')
print("Number of door types",len(door_types))

# Group 9
print("---------Group 9 Results-----------")
settings = ifcopenshell.geom.settings()  
total_wall_area = calculate_wall_area(model, settings)
print(f"Total wall area: {total_wall_area:.2f} square meters")