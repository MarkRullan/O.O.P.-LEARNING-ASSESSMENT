#L.A. #11
#Mark J. Rullan

class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def describePhone(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")

class Android(Phone):
    def __init__(self, brand, model):
        super().__init__(brand, model)

android_phone = Android("Samsung", "Galaxy S23")

android_phone.describePhone()
