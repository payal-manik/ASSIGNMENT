# write a function to return the fibonaccie series


def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        temp = a + b
        a = b
        b = temp
        print(a, end=' ')

n = int(input("Enter range: "))
fibonacci(n)
