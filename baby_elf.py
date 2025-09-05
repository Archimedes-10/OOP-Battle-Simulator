from enemy import Kenny_Clark

class baby_elf(Kenny_Clark):
    def cry():
        #New attribute
        print("WAAAHHHHHHHHHH")
    def take_damage(self, damage):
        #Overriding take damage
        print("WHY ARE YOU ATTACKING A BABY YOU MONSTER!")
        return super().take_damage(damage)
    
    