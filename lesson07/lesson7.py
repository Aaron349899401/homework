# Lesson 7
from random import randrange
DC = int(input("what is your DC?: "))
D20 = randrange(1, 20)
print(f"you rolled {D20}")
if DC > D20:
    print("You LOSE!")
else:
    print("You WIN!")