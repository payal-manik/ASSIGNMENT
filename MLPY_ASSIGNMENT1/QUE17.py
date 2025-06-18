# print ASCII values of characters in a string

string = str(input("Enter any string:"))

for i in string:
    print("ASCII of ", i ," = ",ord(i))