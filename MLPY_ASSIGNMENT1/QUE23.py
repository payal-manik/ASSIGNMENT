# find factorial of a number

num = int(input("Enter any number:"))

fact = 1
for i in range(1,num+1):
    fact = fact * i
    num = num - 1
print("Factorial = ",fact)