# this is what we will use for the video intro to dictionaries

# dictonary - a collection of {key:value} pairs ordered and changeable. No duplicates

# ID:Name


capitals = {"USA": "Washington D.C.",
             "India": "New Deli",
               "China":"Beijing",
                 "Russia": "Moscow"}



print(dir(capitals))
# print(help(capitals))

print(capitals.get("USA"))

print(capitals.get("Japan"))

if capitals.get("Japan"):
    print("Exists")
else:
    print("Doesn't exist")

capitals.update({"Germany":"Berlin:"})


capitals.update({"USA": "Detroit"})


capitals.pop("China")
capitals.popitem()
capitals.clear()

keys = capitals.keys()

for key in capitals.keys():
    print(key)



values = capitals.values()
print(values)


for value in capitals.values():
    print(value)




items = capitals.items()
print(items)


for key, value in capitals.items():
    print(f"{key}: {value}")