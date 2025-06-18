# print sum of digits of a number

num = int(input("Enter any number:"))

sum = 0
dg = 0
while (num > 0):
    dg = num % 10
    sum = sum + dg
    num = num // 10
print("Sum of digits of number = ",sum)