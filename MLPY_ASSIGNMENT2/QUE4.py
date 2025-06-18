# write a function to reverse a string

def rev_str(s):
    re_str = ""
    for ch in s:
        re_str = ch + re_str
    return re_str

s = str(input("Enter any string:"))
print("Reverse of string: ",rev_str(s))