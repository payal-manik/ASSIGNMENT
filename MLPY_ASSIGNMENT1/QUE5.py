# print multiplication table of a number

n = int(input("Enter the number of which you want to print multiplication table:"))

for i in range(1,11):
    print(n ,"*", i ,"=", n*i)