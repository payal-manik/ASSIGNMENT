# write a function to check if string is palindrome or not

# re_str = ""
def rev_str(s):
    re_str = ""
    for ch in s:
        re_str = ch + re_str
    if(s == re_str):
        return True
    else:
        return False

s = str(input("Enter any string:"))

print("Is palindrome:",rev_str(s))