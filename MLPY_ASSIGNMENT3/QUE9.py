# Demonstrate single inheritance in Python. 


class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")


dog1 = Dog()

dog1.sound()  
dog1.bark()   
