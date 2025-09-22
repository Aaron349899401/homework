# Lesson 11
coordinate = input("Enter the coordinates: ")
x, y = coordinate.split(", ")
x, y = map(int, (x, y))
def main():
    if x > 0:
        if y > 0:
            print("You are in Quadrant 1")
        elif y < 0:
            print("You are in Quadrant 4")
    elif x < 0:
        if y > 0:
            print("You are in Quadrant 2")
        elif y < 0:
            print("You are in Quadrant 3")
    elif x == 0 and y == 0:
        print("You are at the ORIGIN!")
    elif x == 0:
        print("You are at the y-axis")
    elif y == 0:
        print("You are at the x-axis")
main()
