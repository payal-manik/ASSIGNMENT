# Create two objects of a class and demonstrate that they are independent. 

class car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
        
    def display(self):
        print("Brand is ",self.brand)
        print("Color is ",self.color)
        

car1 = car("Mercedes-Benz","Black")
car2 = car("Rolls Royce","Pastel Green")

print("Car 1 details:")
car1.display()
print("\nCar 2 details:")
car2.display()