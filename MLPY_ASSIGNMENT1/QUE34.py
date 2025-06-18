# find common elements in two lists

l1 = [1,2,10,13,30,4,5,6]
l2 = [7,8,9,10,13,5,2,25]

cmn = []

for i in l1:
    for j in l2:
        if i == j and i not in cmn:
            cmn.append(i)

print("Common elements:", cmn)