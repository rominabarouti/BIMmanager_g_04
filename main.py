import ifcopenshell
from external.Group1.Heightfloor2floorRule import checkRule as floor2FloorHeight
from external.Group2.rules.deskRule import checkRule as deskRule
from external.Group6.rules.curtainWalls import checkRule as curtainWalls
from external.Group8.rules.numberofDoor import checkRule as numberOfDoors
from external.Group8.rules.doorType import checkRule as doorTypes

model_path = "C:/Users/romin/Desktop/Advanced Bilding information modelling/CES_BLD_24_06_ARC.ifc"
model = ifcopenshell.open(model_path)


# Group 1 
print("---------Group 1 Results-----------")
floor2FloorHeight(model)

# Group 2 
print("---------Group 2 Results-----------")
desk_results = deskRule(model)
print(f"Total Desks: {desk_results[0]}")
print(desk_results[1])


# Group 6 
print("---------Group 6 Results-----------")
curtainWalls(model)

# Group 8 
print("---------Group 8 Results-----------")
print(numberOfDoors(model))
print(doorTypes(model))


""" roofs = model.by_type('Ifcroof')
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
print(f"Total wall area: {total_wall_area:.2f} square meters") """
