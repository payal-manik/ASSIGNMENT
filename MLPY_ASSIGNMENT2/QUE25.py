# Create a function that checks if a number is an Armstrong number.

def armstrong_num (num ):
    temp = num
    sum = 0
    n = len(str(num))
    while(num != 0):
        dg = num % 10
        sum = sum + (dg ** n)
        num = num // 10
    return sum == temp


num = int(input("Enter a number:"))
print("Is Armstrong : ",armstrong_num(num))