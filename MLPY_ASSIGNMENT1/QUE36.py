# print right-angled triangle pattern

n = int(input("Enter no of rows:"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()