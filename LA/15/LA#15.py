#L.A. #15
#Mark J. Rullan

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass 

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f"{self.name} says: Bark!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f"{self.name} says: Meow!")

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f"{self.name} says: Chirp!")

class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f"{self.name} says: ...")

dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Chirpy")
fish = Fish("Goldie")

for animal in (dog, cat, bird, fish):
    animal.speak()
