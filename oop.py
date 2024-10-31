class Fruits:
    # Constructor method
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

    # Display method (corrected spelling and indentation)
    def display(self):
        print(f"I love eating {self.name}, it costs {self.price} and it is {self.color}.")

# Instances
myobj = Fruits("banana", 20, "yellow")
myobj.display()

myobj2 = Fruits("apple", 15, "red")
myobj2.display()
