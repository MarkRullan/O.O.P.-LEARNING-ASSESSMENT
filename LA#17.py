#L.A. #17
#Mark J. Rullan

class Player:
    def __init__(self, name, health, atk_power):
        self.name = name
        self.health = health
        self.atk_power = atk_power
    def attack(self, target):
        target.health = target.health - self.atk_power
        print(f"{self.name} attack {target.name}!")
        print(f"{self.name} deals {self.atk_power} damage")
        print(f"{target.name} now has only {target.health}")
        
gusion = Player("Gusion", 2578, 200)
lancelot = Player("Lancelot", 2549, 250)
print(gusion.name, gusion.health, gusion.atk_power)
print(lancelot.name, lancelot.health, lancelot.atk_power)

while gusion.health > 0 and lancelot.health > 0:
    gusion.attack(lancelot)
    if lancelot.health <= 0:
        print(f"{lancelot.name} has been defeated! {gusion.name} wins!")
        break
    
    if gusion.health <= 0:
        print(f"{gusion.name} has been defeated! {lancelot.name} wins!")
        break