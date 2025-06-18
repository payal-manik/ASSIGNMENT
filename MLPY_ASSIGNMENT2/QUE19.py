# Create a function that accepts a list of integers and returns only the even ones.

def even_list(li):
    even_li = []
    for i in li:
        if i % 2 == 0:
            even_li.append(i)
    return even_li

li = [10,1,11,30,5,7,12]
print("Even list = ",even_list(li))