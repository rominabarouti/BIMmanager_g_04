import ifcopenshell
from external.Group1.Heightfloor2floorRule import checkRule as floor2FloorHeight
from external.Group2.rules.deskRule import checkRule as deskRule
from external.Group6.rules.curtainWalls import checkRule as curtainWalls
from external.Group8.rules.numberofDoor import checkRule as numberOfDoors
from external.Group8.rules.doorType import checkRule as doorTypes
from external.Group9.rules.wallRule import calculate_wall_area 

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

# Group 9 
total_wall_area = calculate_wall_area(model)
print(f"Total wall area: {total_wall_area:.2f} square meters")
