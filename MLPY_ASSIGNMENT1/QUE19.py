# check if a number is divisible by 2 and 3

num = int(input("Enter any number:"))

if(num % 2 == 0 and num % 3 == 0):
    print("number is divisible by both 2 and 3")
else:
    print("number is not divisible by both 2 and 3")