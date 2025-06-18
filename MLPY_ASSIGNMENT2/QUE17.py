# Write a function that accepts a list and returns the list in reverse order.

def rev_list(li):
    rev = []
    for i in li[::-1]:
        rev.append(i)
    return rev

li = [10,20,30,40,50]
print("Reversed list = ",rev_list(li))