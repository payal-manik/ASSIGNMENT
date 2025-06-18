#  Create a base class and derive two child classes with different methods(multilevel inheritance).

class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def weep(self):
        print("Puppy weeps")

puppy1 = Puppy()

puppy1.sound()
puppy1.bark()
puppy1.weep()