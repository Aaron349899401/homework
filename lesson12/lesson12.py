# Lesson 12
a = int(input("Enter the first angle: "))
b = int(input("Enter the second angle: "))
c = int(input("Enter the third angle: "))
while True:
    abc = [a, b, c]
    if sum(abc) == 180:
        if a == b == c:
            print("You have an Equilateral Triangle!")
        elif a != b or a != c:
            if b == c:
                print("You have an Isosceles Triangle!")
            elif b != c:
                print("You have a Scalene Triangle!")
        elif b != a or b != c:
            if a == c:
                print("You have an Isosceles Triangle!")
            elif a != c:
                print("You have a Scalene Triangle!")
        elif c != a or c != b:
            if a == b:
                print("You have an Isosceles Triangle!")
            elif a != b:
                print("You have a Scalene Triangle!")
    break