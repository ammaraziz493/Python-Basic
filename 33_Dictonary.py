dic={
    "Harry": "Human Being",
    "spoon": "Object",
    546: "Neha"
}
print(dic["Harry"])
print(dic[546]) # it will give an error
print(dic.get("spoon"))
print(dic.keys()) # to get the keys of a dic
print(dic.values())
print(dic.items()) # it will give key value pairs
for key in dic.keys():
    print(f"The value corresponding to the key is {dic[key]}")

for key,value in dic.items():
    print(f"The value corresponding to the key  {key} is {value}")
