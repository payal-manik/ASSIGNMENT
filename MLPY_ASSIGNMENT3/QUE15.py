#  Demonstrate encapsulation using getter and setter.

class Student:
    def __init__(self):
        self.__name = ""  

    
    def set_name(self, name):
        self.__name = name

    
    def get_name(self):
        return self.__name


s1 = Student()

s1.set_name("Alice")
print(s1.get_name())
