import random

class Kenny_Clark:
   
    def __init__(self, name):
        self.name = name
        self.health = 1000
        self.attack_power = random.randint(15, 40)

    def attack(self):
        return random.randint(1, self.attack_power)
    
    def special_attack(self):
        self.sattack = random.randint(0,100)
        if self.sattack == 67:


    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    def is_alive(self):
        return self.health > 0