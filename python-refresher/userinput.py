"""
User Input
"""

first_name = input("Enter your first name: ")
days = input("How many days before your birthday: ")
print(f"Hi {first_name} only {days} days before your birthday!")

"""
Assignment
"""
weeks = round(int(days)/7)
print(f"Hi {first_name} only {weeks} weeks before your birthday!")