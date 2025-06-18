#  Create a class `Employee` with a method to display the number of employees created.


class Employee:
    count = 0 

    def __init__(self):
        Employee.count += 1  
        
    def show_count(self):
        print("Number of employees created:", Employee.count)

e1 = Employee()
e2 = Employee()
e3 = Employee()

e2.show_count()
