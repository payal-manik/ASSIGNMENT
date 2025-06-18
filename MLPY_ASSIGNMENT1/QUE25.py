# reverse a number using loop

n = int(input("Enter a number:"))
rev = 0

while(n > 0):
    dg = n % 10
    rev = rev * 10 + dg
    n = n // 10
print("Reverse number = ",rev)