# Lesson 9
import random
# This part is here to recieve input from the player a
# Also to make sure they only inputted either rock, paper, or scissors
amongus = True

while amongus:
    player = input("What did you choose? (rock, paper, or scissors): ")
    if player in {"rock", "paper", "scissors"}:
        amongus = False
# Something to compare the players result to (the opponent)
CPU = random.choice(["rock", "paper", "scissors"])
print(f"The CPU chose {CPU}")
# Whether or not the player won
if player == CPU:
    print("DRAW")
elif player == "rock":
    if CPU == "scissors":
        print("YOU WIN!")
    else:
        print("YOU LOSE!")
elif player == "paper":
    if CPU == "rock":
        print("YOU WIN!")
    else:
        print("YOU LOSE!")
elif player == "scissors":
    if CPU == "paper":
        print("YOU WIN!")
    else:
        print("YOU LOSE!")
# End of game