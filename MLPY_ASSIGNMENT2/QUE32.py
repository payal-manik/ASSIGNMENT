#  Write a function to find the most frequent element in a list. 

def most_frequent(lst):
    return max(set(lst), key=lst.count)    #set used for remove duplicates from list


numbers = [1, 3, 2, 3, 4, 3, 5]
print(most_frequent(numbers))  
