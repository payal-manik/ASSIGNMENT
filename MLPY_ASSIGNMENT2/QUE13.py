#create a function to find sum of digits of anumber

def sum_of_digit(num):
    sum = 0
    while(num > 0):
        dg = num % 10
        sum = sum + dg
        num = num // 10
    return sum

num = int(input("Enter any number:"))
print("Sum of digits of ",num," = ",sum_of_digit(num))