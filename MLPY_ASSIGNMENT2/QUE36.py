# Write a function that returns a list of tuples (element, index) from a list.

def elem_with_index(lst):
    for i in range(len(lst)):
        print("index of ",lst[i], " = ",i)


li = [10, 20, 30]
elem_with_index(li)

