# create a function to count the number vowels in a string

def count_vowel(s):
    count = 0
    for ch in s:
        if(ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U' or ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
            count = count + 1
    return count
s = str(input("Enter any string:"))
print("No of vowels = ",count_vowel(s))