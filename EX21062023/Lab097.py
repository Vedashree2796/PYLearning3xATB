veda_details2 = \
    {"name": "veda",
     "90": 34.34,
     "isMale": True,
     "Address": "KA"
     }

print(veda_details2.get("Address"))
print(veda_details2["Address"])
print(veda_details2.values())
print(veda_details2.keys())

my_dict = {'a': 1, 'b': 2, 'c': 3, 'a': 94, 'd': 93}  # a,b,c,d are key words & 1,2,3 are values
print(my_dict)
print(len(my_dict))
print(list(my_dict.keys()))
print(list(my_dict.values()))

for k, v in my_dict.items():
    print(k, v)
