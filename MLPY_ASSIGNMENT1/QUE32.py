# check if number is palindrome or not

num = int(input("Enter a number:"))
temp = num
rev = 0

while(num > 0):
    dg = num % 10
    rev = rev * 10 + dg
    num = num // 10
if(rev == temp):
    print("Palindrome")
else:
    print("Not a palindrome")