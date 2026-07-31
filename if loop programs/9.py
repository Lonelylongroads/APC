#Python program to check if a year is leap year or not

year = float(input("Enter year: "))

if year % 4 == 0:
    print("The year is Leap Year.")
else:
    print("The year is not a Leap Year.")