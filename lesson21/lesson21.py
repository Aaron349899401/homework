# Lesson 21
max = 0
num_max = 1

N = int(input("Enter a number: "))
for num in range(1, N + 1):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count > max:
        max = count
        num_max = num

print(f"{num_max} has the most factors within the range of 1 to {N}")