# Create a function to remove duplicates from a list. 

def remove_dupl(li):
    new_li = []
    for i in li:
        if i not in new_li:
            new_li.append(i)
    return new_li

li = [10,20,30,40,40,50,70,70,70,8,8,9,10,50]
print("List without duplicates =", remove_dupl(li))
