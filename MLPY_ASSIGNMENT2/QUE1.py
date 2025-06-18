# write a function to check if a number is prime or not

def prime(n,i=2):
    if(n <= 2):
        return True if n == 2 else False
    if (n % i == 0):
        return False
    if(i * i > n):
        return prime(n,i+1)
    
num = int(input("Enter any number:"))
if(prime):
    print("Prime number")
else:
    print("Not a prime number")