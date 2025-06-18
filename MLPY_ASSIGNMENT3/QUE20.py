# Create a class `Rectangle` with method to calculate area and perimeter.

class Rectangle:
    
    def __init__(self,length,bredth):
        self.length = length
        self.bredth = bredth
        
    def calculate_area(self):
        print("Area = ",self.length * self.bredth)
        
    def calculate_perimeter(self):
        print("Perimeter = ",2*(self.length + self.bredth))
        
rect = Rectangle(5,2)
rect.calculate_area()
rect.calculate_perimeter()