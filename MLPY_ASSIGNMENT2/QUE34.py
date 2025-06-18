# Create a function that finds the intersection of two lists. 

def intersection_list(lst1,lst2):
    intersection = list(set(lst1) & set(lst2))
    return intersection

lst1 = [1,2,3,4,5]
lst2 = [3,4,5,6,7,8,9]

print("Intersection of 2 list = ",intersection_list(lst1,lst2))