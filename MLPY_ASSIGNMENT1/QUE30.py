# count frequency of digit in a number

num = input("Enter a number: ")

for i in range(10):
    count = 0
    for dig in num:
        if dig == str(i):
            count += 1
    if count > 0:
        print("Digit ",i," occurs ",count," times.")

    