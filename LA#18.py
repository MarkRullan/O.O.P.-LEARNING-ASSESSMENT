#L.A. #18
#Mark J. Rullan

class Pizza:
    def __init__(self, size, crust_type, toppings):
        self.size = size
        self.crust_type = crust_type
        self.toppings = toppings

    def __str__(self):
    
        toppings_str = ", ".join(self.toppings)
        return f"A {self.size} pizza with a {self.crust_type} crust, topped with {toppings_str}."

pizza1 = Pizza("large", "thin", ["cheese", "pepperoni", "olives"])
pizza2 = Pizza("medium", "stuffed", ["mushrooms", "sausage", "onions", "cheese"])
pizza3 = Pizza("small", "gluten-free", ["tomato", "basil", "mozzarella"])

print(pizza1)
print(pizza2)
print(pizza3)
