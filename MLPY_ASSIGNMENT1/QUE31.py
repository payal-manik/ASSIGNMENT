# GCD of two numbers using loop

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print("GCD is:", a)