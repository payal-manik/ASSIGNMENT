#  Write a recursive function to compute the factorial of a number.

def fact(num):
    if(num == 0):
        return 1
    elif(num < 0):
        return False
    else:
        return (num * fact(num-1))
    

num = int(input("Enter any number:"))
print("Factorial = ",fact(num))
        