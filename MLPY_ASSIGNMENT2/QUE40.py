# Write a function that counts the number of uppercase and lowercase characters in a string.

def count_upper_lower(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if 'A' <= char <= 'Z':      
            upper_count += 1
        elif 'a' <= char <= 'z':    
            lower_count += 1
    print("Uppercase characters =", upper_count)
    print("Lowercase characters =", lower_count)

s = input("Enter any string: ")
count_upper_lower(s)
