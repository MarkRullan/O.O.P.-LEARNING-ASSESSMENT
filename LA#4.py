#L.A. #4
#Mark J. Rullan

class Character:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def __str__(self):
        return f"{self.name} is a {self.role} hero."
        
    def describe(self):
        print(f"{self.name} is a {self.role} hero.")
    
hero = Character("Xborg", "Fighter")
print(hero)