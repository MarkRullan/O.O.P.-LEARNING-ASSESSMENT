#L.A. #7
#Mark J. Rullan

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        
car1 = Car("Toyota", "black")
car2 = Car("Honda", "White")

print(car1.brand, car1.color)
print(car2.brand, car2.color)

car1.color = "blue"

print(car1.brand, car1.color)
print(car2.brand, car2.color)