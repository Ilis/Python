import json

names = {
    "mama": "Nata",
    "papa": "Ilia",
    "kid1": "Vika",
    "kid2": "Lena"
    }

print(names)

j = json.dumps(names, indent=4)
with open("test.json", "w") as f:
    f.write(j)
del j
