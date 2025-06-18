#  Create a function that returns the median of a list. 

def median(lst):
    s = sorted(lst)
    mid = len(s) // 2
    return (s[mid] + s[-mid-1]) / 2 if len(s) % 2 == 0 else s[mid]


print(median([3,1,4,2,5]))  
print(median([3,1,4,2]))   
