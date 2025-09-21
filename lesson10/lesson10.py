# Lesson 10
# input always returns a string by defult
digits = input("what are the last four digits of your number?: ")
if digits[0] in ["8", "9"]:
    if digits[1] == digits[2]:
        if digits[3] in ["8", "9"]:
            print("Telemarketer")
        else:
            print("Not a Telemarketer")
    else:
        print("Not a Telemarketer")
else:
    print("Not a Telemarketer")