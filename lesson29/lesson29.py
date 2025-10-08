# Lesson 29
string = input("Enter your string: ")

def cons_check(string):
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    count = 0
    for char in string:
        if char in consonants:
            count += 1
    return count

result = cons_check(string)
print(result)
