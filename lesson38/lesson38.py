# Lesson 38
list = []
for first in range(100, 1000):
    for second in range(100, 1000):
        num = str(first * second)
        if num == num[::-1]:
            list.append(int(num))
print(max(list))
            