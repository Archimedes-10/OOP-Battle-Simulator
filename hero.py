import random
from boss import Kenny_Clark

class Hero:


    
    """
    This is our hero blueprint.
    
    O=('-'Q)
    """
    
    def __init__(self, name):
        self.name = name
        self.health = 250
        self.strength = random.randint(30, 70)
   

    def strike(self, special_attack):
        self.attack = random.randint(10,self.strength)
    
    def receive_damage(self, damage):
        self.take_damage = self.health - damage
        if self.take_damage


    def living(self):  
        self.health >0
        # TODO We should prevent health from going into the NEGATIVE
    
    #TODO define is_alive
 

