#  Use `super()` to call a parent class method.

class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")

dog1 = Dog()

dog1.sound()