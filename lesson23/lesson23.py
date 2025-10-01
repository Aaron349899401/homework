# Lesson 23
ching = True
count = 0
total_sum = 0
while ching:
    num = input("Enter you numbers: ")
    if num.lower().capitalize() == "Exit":
        ching = False
        break
    else:
        chong = int(num)
        count += 1
        total_sum += chong

dong = total_sum / count
print(f"The average is {dong}!")

