# sum of even numbers in a list

l = [1,20,5,30,4,9,7,33,14]
sum = 0

for i in l:
    if(i % 2 == 0):
        sum = sum + i
    else:
        i = i + 1
print("Sum of even numbers = ",sum)