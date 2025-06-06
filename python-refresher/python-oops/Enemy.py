class Enemy:
    # type_of_enemy: str
    # health_points: int
    # attack_damage: int

    def __init__(self, type_of_enemy, health_points = 10, attack_damage = 1):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def get_type_of_enemy(self):
        return self.__type_of_enemy
    
    # def set_type_of_enemy(self, type_of_enemy):
    #     self.__type_of_enemy = type_of_enemy

    def talk(self):
        print("I am an enemy!")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} moved closer to you")
    
    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.attack_damage} damage")
    
