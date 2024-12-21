#L.A. #14
#Mark J. Rullan

class Spiderman:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def describeSpiderman(self):
        print(f"Name: {self.name.capitalize()}")
        print(f"Age: {self.age}")

class Tobey(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Andrew(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Tom(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

tobey_spiderman = Tobey("tobey maguire", 46, "Spider-Man 1")
andrew_spiderman = Andrew("andrew garfield", 40, "The Amazing Spider-Man")
tom_spiderman = Tom("tom holland", 28, "Spider-Man: Homecoming")

print(f"{tobey_spiderman.name.upper()} starred in {tobey_spiderman.movieTitle}")
print(f"{andrew_spiderman.name.upper()} starred in {andrew_spiderman.movieTitle}")
print(f"{tom_spiderman.name.upper()} starred in {tom_spiderman.movieTitle}")
