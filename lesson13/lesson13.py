# Lesson 13
month = [1, 12]
day = [1, 31]
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

if month == 2 and day == 18:
    print("Special")
elif month > 2:
    print("After")
elif month < 2:
    print("Before")
elif month == 2:
    if day > 18:
        print("After")
    elif day < 18:
        print("Before")
