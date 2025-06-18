# Write a function to compute the power of a number using recursion. 

def power_of_num(num,exp):
    if(exp == 0):
        return 1
    else:
        return num * power_of_num(num,exp-1)

num = int(input("Enter any number:"))
exp = int(input("Enter a exponent value:"))

print("Power of ",num," = ",power_of_num(num,exp))