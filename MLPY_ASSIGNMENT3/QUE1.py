# Create a simple class `Person` with name and age as attributes. 

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name = ",self.name)
        print("Age = ",self.age)

p1 = person("Vaibhav",21)
p1.display()