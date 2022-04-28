"""
This program demosntrates the use of dictionaries to preform outputs with the theme of Star Trek

Author:Jacob Olshanskiy
Date: 4-26-22
"""
captains = {
    "Enterprise": "Picard",
    "Voyager": "Janeway",
    "Defiant": "Sisko",
}
if "Enterprise" in captains:
    print("Found")
else:
    captains["Discovery"] = ["Unknown"]
print(captains)
if "Discovery" in captains:
    print("Found")
else:
    captains["Discovery"] = ["Unknown"]
for pilots in captains:
    print("The", pilots, "is piloted by", captains[pilots])
captains.pop("Discovery")
print(captains)