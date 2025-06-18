# count vowels in a string

string = str(input("Enter a string:"))
count = 0

for i in string:
    if(i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' or i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        count = count + 1
print("No of vowels in string is ",count)