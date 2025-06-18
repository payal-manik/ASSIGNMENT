# Demonstrate method overriding in inheritance. 

class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")


dog1 = Dog()

dog1.sound()