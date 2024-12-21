#L.A. #3
#Mark J. Rullan

class Character:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        
    def describe(self):
        print(f"{self.name} is a {self.role} hero.")
    
hero = Character("Xborg", "Fighter")
hero.describe()
