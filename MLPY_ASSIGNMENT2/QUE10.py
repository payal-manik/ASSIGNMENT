#write the function to find minimum number of a list

def min_num(a,b,c):
    return min(a,b,c)
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
print("Smallest number = ",min(a,b,c))