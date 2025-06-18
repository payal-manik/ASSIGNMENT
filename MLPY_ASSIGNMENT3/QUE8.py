# Demonstrate use of `isinstance()` with a class

class Animal:
    def __init__(self, name):
        self.name = name
        
a1 = Animal("Dog")

print(isinstance(a1, Animal))  
print(isinstance(a1, str)) 