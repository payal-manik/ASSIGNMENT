#  Demonstrate constructor overloading using default arguments.

class Person:
    def __init__(self, name="MANIK"):
        self.name = name

    def show(self):
        print("Name:", self.name)

p1 = Person()
p2 = Person("Alice")

p1.show()
p2.show()
