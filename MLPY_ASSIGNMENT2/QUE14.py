# write a function that takes a string and returns a dictionary of character frequencies

def char_freq(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

input_str = input("Enter a string: ")
result = char_freq(input_str)
print(result)
