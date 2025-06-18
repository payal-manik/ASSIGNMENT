# create a function to find the maximum of three numbers

def max_num(a,b,c):
    return max(a,b,c)
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
print("Largest number = ",max(a,b,c))