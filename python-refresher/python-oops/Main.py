"""
4 pillars of OOPs

Encapsulation
Abstraction
Inheritance
Polymorphism
"""

# from Dog import *

# dog = Dog()

# dog.legs;
# dog.ears;
# dog.type;
# dog.age;
# dog.color;

# -------

from Enemy import *

# enemy = Enemy()

# enemy.type_of_enemy = "Zombie"

# enemy.talk()

# enemy.walk_forward()

# enemy.attack()

# print(f"{enemy.type_of_enemy} has {enemy.health_points} health_points And can do attack of {enemy.attack_damage}")

# ------ constructors

zombie = Enemy("Zombie",1,10)
big_zombie = Enemy("Big Zombie", 10,100)
vampire = Enemy("Vampire")




print(zombie.get_type_of_enemy())



# ----- Encapsulation is bundling of data
