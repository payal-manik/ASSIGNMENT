# Create a function to merge two sorted lists into one sorted list.

def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)


a = [1, 3, 5]
b = [2, 4, 6]
print(merge_sorted_lists(a, b))  
