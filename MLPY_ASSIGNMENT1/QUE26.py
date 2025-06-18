# find the maximum in a list using loop

li = [10,85,32,30,47,90]
max_val = li[0]

for i in li:
    if(i > max_val):
        max_val = i
print("Maximum number = ",max_val)