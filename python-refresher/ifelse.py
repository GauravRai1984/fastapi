"""
Flow Control: If Else Elif
"""
x = 2
if x > 1:
    print("x is greater than 1")
else:
    print("x is not greater than")

print("outside of if statement")

hour = 21
if hour < 15:
    print("good morning")
elif hour < 20:
    print("good evening")
else:
    print("good night")

"""
Assignment
"""
grade = 87

if grade >=90:
    print("A")
elif grade >= 80 and grade <90:
    print("B")
elif grade >= 70 and grade <80:
    print("C")
elif grade >= 60 and grade <70:
    print("D")
else:
    print("F")