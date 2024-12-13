#O.E. #4
#Mark J. Rullan

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        target.health -= self.power
        print(f"{self.name} attacks {target.name} for {self.power} damage!")
        print(f"{target.name}'s health is now {target.health}.\n")

    def special_move(self):
        pass  
    def defend(self, attacker):
        damage_taken = attacker.power // 2  
        self.health -= damage_taken
        print(f"{self.name} defends and reduces damage by half. {self.name}'s health is now {self.health}.\n")


class Warrior(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    def special_move(self):
        self.power *= 2
        print(f"{self.name} uses Shield Bash! Attack power is now {self.power}.\n")


class Mage(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    def special_move(self):
        print(f"{self.name} casts Fireball! {self.name} deals 100 damage to the target.\n")
        return 100 

class Archer(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    def special_move(self):
        print(f"{self.name} shoots a Piercing Arrow! Damage ignores target's defense.\n")
        return self.power 


class Monster(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    def special_move(self):
        self.health += 50 
        print(f"{self.name} roars and gains 50 health! {self.name}'s health is now {self.health}.\n")


warrior = Warrior("Warrior", 200, 30)
mage = Mage("Mage", 150, 25)
archer = Archer("Archer", 120, 20)
monster = Monster("Monster", 300, 40)

characters = [warrior, mage, archer]

while monster.health > 0:
    for character in characters:
        print(f"{character.name}'s turn:")
        
        character.attack(monster)
        
        special_damage = character.special_move()
        
        if special_damage:
            monster.health -= special_damage
        
        print(f"{monster.name}'s health after the turn: {monster.health}")
        print(f"{character.name}'s health after defending: {character.health}\n")
        
        if monster.health <= 0:
            print(f"{monster.name} has been defeated!")
            break
        
        monster.attack(character)
        monster.special_move()
        
        character.defend(monster)

for character in characters:
    if character.health <= 0:
        print(f"{character.name} has been defeated.")
