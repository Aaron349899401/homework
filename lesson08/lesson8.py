# Lesson 8
Wins = 0
for i in range(6):
    result = input(f"Enter result of game {i+1}: ")
    if result == "w" or "W":
        Wins += 1

group = 69
if Wins > 4:
    group = 1
elif Wins > 2:
    group = 2
elif Wins > 0:
    group = 3

if group == 0:
    print("You have been eliminated")
else:
    print(f"You are in group {group}!")

