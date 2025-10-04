# Lesson 3
import math
num = int(input("Enter a number: "))
side_length = math.floor(math.sqrt(num))
largest_area = side_length * side_length
print(f"The largest possible area for your input value is {largest_area}")
print(f"The side length of this square is {side_length}")