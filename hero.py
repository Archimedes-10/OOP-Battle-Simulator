import random

class Hero:


    
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
       
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    
    def __init__(self, name):
        self.name = name
        self.health = 250
        self.strength = random.randint(30, 70)
    

    def strike(self):
        self.attack = random.randint(10,self.strength)
    
    def receive_damage(self, damage):
        self.take_damage = 
        # TODO Implement take_damage
        # TODO We should prevent health from going into the NEGATIVE
    
    #TODO define is_alive
