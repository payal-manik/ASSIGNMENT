#  Create a function to calculate the greatest common divisor (GCD) of two numbers. 

def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
print("GCD =", gcd(a, b))
