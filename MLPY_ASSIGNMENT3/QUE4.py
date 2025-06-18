# Create a private attribute in a class and access it using a method.


class author:
    
    def __init__(self,name):
        self.__name = name
        
    def get_name(self):
        return self.__name
    
a1 = author("mann_ruh")
print("Author name is ",a1.get_name())