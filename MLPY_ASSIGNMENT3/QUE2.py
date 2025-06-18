# Add a method to the `Person` class that prints a greeting. 

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name = ",self.name)
        print("Age = ",self.age)
    def greets(self):
        print("Hello!! Good morning")

p1 = person("Vaibhav",21)
p1.display()
p1.greets()