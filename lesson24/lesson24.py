# Lesson 24
sigma = True
length = []
while sigma:
    noway = input("Enter your word: ")
    if noway.capitalize() == "X":
        sigma = False
        break
    else:
        length.append(noway)

ofcourse = max(length, key=len)

print(f"The longest word is {ofcourse}")