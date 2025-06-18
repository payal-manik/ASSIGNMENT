# Write a function to find the second largest number in a list. 

def second_largest(li):
    li = list(set(li))    
    li.sort()             
    if len(li) >= 2:
        return li[-2]     
    else:
        return None      

li = [10, 20, 40, 30, 50]
print("Second largest =", second_largest(li))
