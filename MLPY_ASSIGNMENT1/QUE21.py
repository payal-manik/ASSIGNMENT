# swap two numbers using a temporary variable

a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))

print("Before swapping value of a & b is ",a,"&",b)

temp = a
a = b
b = temp

print("After swapping value of a & b is ",a,"&",b)