class Person:
    # Constructor method
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # Display method
    def display(self):
        print(f"My name is {self.name}, my age is {self.age}, and my gender is {self.gender}.")

# Creating an instance of the Person class
myobj = Person(name="Fathi", age=21, gender="female")
myobj.display()
