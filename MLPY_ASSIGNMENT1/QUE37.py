# check if a year is leap year or not

year = int(input("Enter year tou want to check:"))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")