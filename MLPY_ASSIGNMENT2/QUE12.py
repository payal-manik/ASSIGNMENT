# write a function to check number is perfect

def perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False

n = int(input("Enter a number: "))
if perfect(n):
    print(n, "is a perfect number.")
else:
    print(n, "is not a perfect number.")
