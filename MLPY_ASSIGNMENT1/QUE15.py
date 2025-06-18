# check if a number is divisible by both 3 and 5

num = int(input("Enter any number:"))

if(num % 3 == 0 and num % 5 == 0):
    print("number is divisible by both 3 and 5")
else:
    print("number is not divisible by both 3 and 5")