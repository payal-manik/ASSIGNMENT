# Write a program to demonstrate polymorphism with a common method. 


class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")


dog1 = Dog()
cat1 = Cat()

dog1.sound()
cat1.sound()
