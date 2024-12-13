#L.A. #9
#Mark J. Rullan

class Car:
    def __init__(self, brand, ):
        self.brand = brand
        
    def __str__(self):
        return f"This object is based on Car class"
        
car = Car("Toyota")
print(car)
del car
print(car)