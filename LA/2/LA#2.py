#L.A. #2
#Mark J. Rullan

class hero:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        
hero1 = hero("Xborg", "Fighter")
hero2 = hero("Khufra", "Tank")
print(hero1.name, hero1.role, "\n", hero2.name, hero2.role)