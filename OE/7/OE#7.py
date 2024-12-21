#O.E. #7
#Mark J. Rullan

class TekkenCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
        
    def introduce(self, func):
        def wrapper():
            print("introducing...")
            func()
            print("This character is amazing!")
        return wrapper
        
character = TekkenCharacter("Raven", "Shadow Clones")

@character.introduce
def character_intro():
    print(f"I am {character.name} and I can use {character.ability}.")
character_intro()