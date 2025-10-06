# Lesson 28
string = str(input("Enter your Palidrome: "))
reversed_string = string[::-1]
if string == reversed_string:
    print("PALINDROME!")
else:
    print("Not a PALINDROME!")