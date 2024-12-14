class Pinakbet:
    def __init__(self, squash, eggplant, okra, yard_long_beans, bitter_melon):
        self.__squash = squash
        self.eggplant = eggplant
        self.okra = okra
        self.yard_long_beans = yard_long_beans
        self.bitter_melon = bitter_melon
        
    def __str__(self):
        return (
            f"Ang pakbet ko may mga gulay na {self.__squash}, "
            f"{self.eggplant}, {self.okra}, {self.yard_long_beans}, {self.bitter_melon}"
        )
        
    def may_kalabasa_ba(self):
        return self.__squash

pinakbet = Pinakbet("garlic", "onions", "tomatoes", "shrimp paste", "salt")

print(pinakbet.may_kalabasa_ba())