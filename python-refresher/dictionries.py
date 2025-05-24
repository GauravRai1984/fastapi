"""
Dictionaries - key- value pairs
"""

user_dictionary = {
    "username": "codinwithroby",
    "name": "Eric",
    "age": 32
}

user_dictionary["married"] = True

for x in user_dictionary:
    print(x)

for x,y in user_dictionary.items():
    print(x,y)

user_dictionary2 = user_dictionary.copy()
user_dictionary2.pop("age")
print(user_dictionary)

user_dictionary2 = user_dictionary
user_dictionary2.pop("age")
print(user_dictionary)

# print(user_dictionary)
# print(user_dictionary["age"])
# print(user_dictionary.get("name"))
# print(len(user_dictionary))
# user_dictionary.pop("age")
# print(user_dictionary)
# user_dictionary.clear()
# print(user_dictionary)


"""
Assignment
"""
my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

for key, value in my_vehicle.items():
    print(key,value)

vehicle2 = my_vehicle.copy()

vehicle2["number_of_tires"] = 4
vehicle2.pop("mileage")
for key in vehicle2:
    print(key)