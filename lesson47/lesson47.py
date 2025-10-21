# Lesson 47
def among(us):
    if us < 1:
        return "Bruh"
    result = 0
    for num in range(1, us + 1):
        result += num
    return result

us = int(input("Enter your positive integer: "))
print(among(us))