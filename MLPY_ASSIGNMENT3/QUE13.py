#  Create an abstract base class using `abc` module.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass 

class Dog(Animal):
    def sound(self):
        print("Dog barks")

dog1 = Dog()
dog1.sound()

