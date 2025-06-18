# Create a class with a method that returns the square of a number. 

class square_of_number:
    
    def __init__(self,number):
        self.number = number
        
    def cal_sq(self):
        result = self.number * self.number
        return result
    
obj = square_of_number(5)
print("Square of 5 = ",obj.cal_sq())