#L.A. #19
#Mark J. Rullan

class Pinakbet:
    def __init__(self, squash, eggplant, okra, yard_long_beans, bitter_melon):
        self.__squash = squash
        self.eggplant = eggplant
        self.okra = okra
        self.yard_long_beans = yard_long_beans
        self.bitter_melon = bitter_melon
        

    def __str__(self):
        return f"Ang pakbet ko may mga gulay na {self.squash}, {self.eggplant}, {self.okra}, {self.yard_long_beans}, {self.bitter_melon}"

pinakbet = Pinakbet("garlic", "onions", "tomatoes", "shrimp paste", "salt")
pinakbet2 = Pinakbet("kalabasa", "talong", "okra", "sitaw", "ampalaya")
pinakbet3 = Pinakbet("kalabasa", "talong", "okra", "sitaw", "ampalaya")

print(pinakbet)
print(pinakbet2)
print(pinakbet3)