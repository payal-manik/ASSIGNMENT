# Write a function to check if all characters in a string are unique. 

def all_unique(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True


s = input("Enter a string: ")
if all_unique(s):
    print("All characters are unique.")
else:
    print("Characters are not unique.")
