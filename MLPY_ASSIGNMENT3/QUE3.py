# Create a class with a class variable and instance variable. 

class student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    def display_detail(self):
        print("Name of student is ",self.name)
        print("Grade of student = ",self.grade)
        
s1 = student("Rashvik","A+")
s2 = student("Ekansh","A")
s1.display_detail()
s2.display_detail()