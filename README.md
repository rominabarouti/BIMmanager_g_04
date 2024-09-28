# BIM Manager Group 04

Following is a summary of group reports with different focus areas within the architectural discipline for assignment 1.  

## Group 1

**Focus Area: Ceilings**

The team focused on verifying the floor-to-floor height of each story in the building to ensure it matches the claim made in the architectural report.

To perform this analysis, the team used a script to examine all objects in the Blender file representing building stories. These objects, identified by names containing "IfcBuildingStorey", were analyzed to determine their heights (Z-coordinates).

The floors were sorted from lowest to highest based on their elevation. The script calculated the elevation difference between adjacent floors (e.g., floor 1 and floor 2, floor 2 and floor 3) by subtracting the Z-coordinate of the lower floor from that of the upper floor. The result showed that the floor-to-floor height was **3.8** meters.

This confirmed the building's floor-to-floor height was consistent with the stated claim in the architectural report.

[Group 1 Repository](https://github.com/Navairax/Group1)

## Group 2

**Focus Area: Desks**

The team focused on verifying the total number of desks in the building. The script was used to identify the number of total desks in the building, revealing **1,620** desks in total. The team used code that interacts with an IFC (Building Information Model) file to count desks across different storeys of the building. The process involved:

- Loading the model using IfcOpenShell
- Identifying all storeys and compiling them into a list called *storeys*

For each storey, the code searched for objects categorized as IfcFurniture or IfcFurnishingElement that contain the term *desk*. It created a list of desks on each storey and calculated the total number of desks by summing up all the desks in the building.

[Group 2 Repository](https://github.com/JohnDope90/Group2)

## Group 6

**Focus Area: Facade**

The team analyzed the facade transparency of the building, where the facade transparency should be **37%**.

The team used a script to calculate transparency by measuring the number of windows and plates on the facade. Initially, the script found that the windows were mislabeled in the model, requiring the use of IfcPlate (for windows) and IfcCurtainWall (for plates) to perform the count.

However, due to inconsistencies in the BIM model, with some windows being mislabeled or placed in different areas, the exact numbers were difficult to determine. Based on the script’s results:

    - IfcCurtainWall (plates) = 2,818
    - IfcPlate (windows) = 1,509

Using these values, the calculated facade transparency was **53.5%**, which differed significantly from the **37%** stated in the report. This discrepancy indicated that the BIM model was inaccurately labeled, leading to a higher transparency ratio than expected.

[Group 6 Repository](https://github.com/Raghadhamza/Group6)

## Group 8

**Focus Area: Doors**

The team analyzed the architectural aspect of doors in the project. The team aimed to determine:

1. Total number of doors in the building
2. Different types of doors used in the building

*numberOfDoor* script was used to find the total number of doors, yielding a result of **664** doors. *doorType* script was used to identify the number of different door types, revealing **33** distinct door types. These scripts specifically targeted objects named IfcDoor and IfcDoorType in the project's data to generate the results.

[Group 8 Repository](https://github.com/Ajad2024/Group8)


## Group 9

**Focus Area: Walls/Floors**

The team used a script to determine: 

- Total number of walls in the building  
- Total number of floors in the building

The script returned **1,715** for the number of walls and **23** for the total number of floors.

[Group 9 Repository](https://github.com/Noahnox/Group9)