my_dict = {
    "class" : "animal",
    "name" : "Mittal",
    "age" : 27
}

print(my_dict)
print(my_dict['name'])
print(my_dict.get("name"))
print(my_dict.values())

for x in my_dict:
    print(my_dict[x])
    
for x,y in my_dict.items():
    print(x,y)
    
my_dict["name"] = "Trivedi"
print(my_dict)

my_dict["city"] = "Ahmedabad"
print(my_dict)

my_dict.pop("city")
print(my_dict)

my_dict.popitem()
print(my_dict)

del my_dict["class"]
print(my_dict)

my_dict.clear()
print(my_dict)

del my_dict
