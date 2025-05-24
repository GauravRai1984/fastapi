"""
For and while loops
"""

my_list = [1,2,3,4,5]
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])

for iterator in my_list:
    print(iterator)

print("<<<>>>")

sum = 0
for x in range(6):
    sum += x

print(sum)

my_str_list = ["Monday","Tuesday","Wednesday","Thursday"]
for x in my_str_list:
    print(f"Happy {x}!!")

i = 0
while i < 5:
    i+=1
    if i == 3:
        continue
    print(i)
    if i == 4:
        break
else:
    print("i is now larger or equal to 5")


"""
Assignment
"""
my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for x in my_list:
    if x == "Monday":
        continue

    for i in range(3):
        print(x + " ", end=" ")
    
    print("\n")

    
