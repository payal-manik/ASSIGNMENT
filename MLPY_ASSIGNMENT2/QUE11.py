#create a function to count howmany times a character appears in a string

def char_freq(s):
    counted = []  
    for char in s:
        if char not in counted:
            count = 0
            for ch in s:
                if ch == char:
                    count += 1   
            print("Character", char, "occurs", count, "times.")
            counted.append(char)

s = input("Enter a string: ")
char_freq(s)

