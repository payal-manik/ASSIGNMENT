#  Create a function that accepts a list and a value, and returns the index of the value (or -1). 

def find_index(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1  


my_list = [10, 20, 30, 40]
print(find_index(my_list, 30))  
print(find_index(my_list, 50)) 
