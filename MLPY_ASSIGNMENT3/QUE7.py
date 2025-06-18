# Create a class and use a method to set its attributes. 

class Book:
    
    def __init__(self,Author,Title):
        self.__Author = Author
        self.Title = Title
        
    def get_Author(self):
        return self.__Author
    
    def set_author(self,new_author):
        self.__Author = new_author
        
    def get_title(self):
        print("Title of Book is ",self.Title)
        
print("Details of author:") 
b1 = Book("Ana Huang","The beats of hearts")
print("Author is ",b1.get_Author())
b1.get_title()

print("\nAfter setting new details of author:") 
b1.set_author("mann_ruh")
print("Author is ",b1.get_Author())
b1.get_title()