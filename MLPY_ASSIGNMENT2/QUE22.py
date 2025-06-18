# Write a function to find the least common multiple (LCM) of two numbers. 


def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
print("LCM =", lcm(a, b))
