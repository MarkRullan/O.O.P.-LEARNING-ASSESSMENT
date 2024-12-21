#L.A. #10
#Mark J. Rullan

class Vehicle:
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
    
    def describeVehicle(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Fuel Type: {self.fuel_type}")

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

car = Car("Toyota", "Corolla", "Gasoline")
motorcycle = Motorcycle("Harley-Davidson", "Sportster", "Gasoline")

print("Car Details:")
car.describeVehicle()

print("\nMotorcycle Details:")
motorcycle.describeVehicle()
