#L.A. #21
#Mark J. Rullan

class IceCream:
    def __init__(self, flavor, whole_milk, heavy_cream):
        self._flavor = flavor 
        self.__whole_milk = whole_milk
        self.heavy_cream = heavy_cream  
        
    def __str__(self):    
        return f"My ice cream is {self._flavor} flavor and has {self.__whole_milk} and {self.heavy_cream} ingredients."
    
    def has_milk(self):
        return self.__whole_milk  
    
    def set_milk(self, new_milk):
        self.__whole_milk = new_milk

chocolate = IceCream("Chocolate", "Whole Milk", "Heavy Cream")
matcha = IceCream("Matcha", "Whole Milk", "Heavy Cream")
vanilla = IceCream("Vanilla", "Whole Milk", "Heavy Cream")
chocolate.set_milk("5% Milk")

print(chocolate)
print(matcha)
print(vanilla)
print(chocolate.has_milk())
