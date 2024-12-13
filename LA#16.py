#L.A. #15
#Mark J. Rullan

class Appliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def operate(self):
        print("Operating!")

    def describe(self):
        print(f"Brand: {self.brand}, Model: {self.model}") 

class WashingMachine(Appliance):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def operate(self):
        print("Washing clothes!")
        
class Refrigerator(Appliance):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def operate(self):
        print("Keeping food cold!")

class Microwave(Appliance):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def operate(self):
        print("Heating food!")

washing_machine = WashingMachine("LG", "WM1234")
refrigerator = Refrigerator("Samsung", "RF1234")
microwave = Microwave("Panasonic", "MW1234")

appliances = [washing_machine, refrigerator, microwave]

for appliance in appliances:
    appliance.describe()
    appliance.operate()
    print()