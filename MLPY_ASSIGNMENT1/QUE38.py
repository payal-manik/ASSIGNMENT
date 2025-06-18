# print fibonaccie series using loop

n = int(input("Enter range: "))

a = 0
b = 1

for i in range(n):
    print(a)
    temp = a + b
    a = b
    b = temp
