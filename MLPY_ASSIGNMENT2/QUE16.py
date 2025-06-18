# Create a function that accepts a number and prints its multiplication table. 

def table(num):
    for i in range(1,11):
        print(num, "*", i ," = ",num * i)
        
num = int(input("Enter any number: "))
table(num)