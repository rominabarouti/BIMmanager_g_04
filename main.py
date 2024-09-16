import ifcopenshell

from external.Group6.rules import doorRule, windowRule
model = ifcopenshell.open("path/to/ifcfile.ifc")

windowResult = windowRule.checkRule(model)
doorResult = doorRule.checkRule(model)

print("Window result:", windowResult)
print("Door result:", doorResult)
