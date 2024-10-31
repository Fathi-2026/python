#fibonacci(100)


# ineritance

class Parent:
    def __init__(self):
        def greet(self):
            return f"i am parent"
class Child(Parent):
    def greet(self):
        return f"i am child"

child=Child()
print(child.greet())

