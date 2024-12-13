#L.A. #12
#Mark J. Rullan

class Toy:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def display_details(self):
        print(f"Toy Name: {self.name}")
        print(f"Price: P{self.price}")

class Car(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)

car_toy = Car("Toy Car", 150)

car_toy.display_details()
