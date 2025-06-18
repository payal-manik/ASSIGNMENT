# create a function to calculate sum of list of numbers

def sum_list(li):
    sum = 0
    for i in li:
        sum = sum + i
    return sum

print("Sum = ",sum_list([10,20,30,40,50]))