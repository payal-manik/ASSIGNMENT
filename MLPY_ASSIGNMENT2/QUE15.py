# write a function that return average of list  of numbers

def avg(li):
    sum = 0
    for i in li:
        sum = sum + i
        avg = sum / len(li)
    return avg
    
li = [10,20,30,40,50]
print("Average = ",avg(li))