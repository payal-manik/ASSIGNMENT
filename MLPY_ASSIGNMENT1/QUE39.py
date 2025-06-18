# count uppercase and lowercase letters in a string

s = str(input("Enter a string:"))

uppercase_count = 0
lowercase_count = 0

for i in s:
    ascii_val = ord(i)
    if(ascii_val >= 65 and ascii_val <= 90):
        uppercase_count += 1
    elif(ascii_val >= 97 and ascii_val <= 122):
        lowercase_count += 1
print("No of uppercase character = ",uppercase_count)
print("No of lowercase character = ",lowercase_count)