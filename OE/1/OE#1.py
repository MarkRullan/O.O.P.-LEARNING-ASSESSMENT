#O.E. #1
#Mark J. Rullan

class Hero:
    def __init__(self, name, role, damage_type):
        self.name = name
        self.role = role
        self.damage_type = damage_type
    
    def __str__(self):
        return f"{self.name} is a {self.role} hero with {self.damage_type} type."
        
    def describe(self):
        print(f"{self.name} is a {self.role} hero with {self.damage_type} type.")
        
    def section(self):
        return f"{self.name} is a {self.role} hero with {self.damage_type} type."
    
hero = Hero("Xborg", "Fighter", "Physical")
print(hero.section())
hero = Hero("Khufra", "Tank", "Physical")
print(hero)
hero = Hero("Natan", "Marksman", "Magical")
hero.describe()
hero = Hero("Gusion", "Assassin", "Magical")
hero.describe()
hero = Hero("Nana", "Mage", "Magical")
hero.describe()