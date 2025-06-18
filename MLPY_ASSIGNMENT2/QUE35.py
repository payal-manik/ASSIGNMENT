# Write a function that accepts variable number of arguments and returns their product.


def product_of_numbers(a,b,c,d,e):
    return a*b*c*d*e

a = int(input("Enter value of a:"))
b = int(input("Enter values of b:"))
c = int(input("Enter values of c:"))
d = int(input("Enter values of d:"))
e = int(input("Enter values of e:"))
print("Product = ",product_of_numbers(a,b,c,d,e))