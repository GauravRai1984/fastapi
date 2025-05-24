"""
Functions
"""

print("Hello and welcome to functions")

def my_function():
    print("inside my_function")

my_function()

def print_my_name(name):
    print(f"hello my name is {name}")

print_my_name("Gaurav")

def print_numbers(highest_number, lowest_number):
    print(highest_number)
    print(lowest_number)

print_numbers(lowest_number=3,highest_number=16)

def multiply_numbers(a,b):
    return a * b

solution = multiply_numbers(10,6)
print(solution)

def print_list(list_of_number):
    for x in list_of_number:
        print(x)

number_list = [1,2,3,4,5]
print_list(number_list)

def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)

def add_tax_to_item(cost_of_item):
    return cost_of_item*0.1

final_cost = buy_item(50)
print(final_cost)

"""
Assignment
"""
def return_dict(firstname, lastname, age):
    my_dict = {
        "firstname": firstname,
        "lastname": lastname,
        "age": age
    }
    return my_dict

print(return_dict("gaurav", "rai","40"))