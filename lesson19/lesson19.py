# Lesson 19
num = int(input("Enter a number: "))
count = True
if count > 2:
    count = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            count = False
            break

if count:
    print("PRIME!")
else:
    print("Not PRIME!")
     