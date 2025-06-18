# Write a function to check if a list is sorted. 

def sort_list(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return True
        else:
            return False
    
lst = [90,80,70,60,50,40,30,20,10]
print("Is Sorted : ",sort_list(lst))