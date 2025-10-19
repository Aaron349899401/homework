# Lesson 42
def skibidi(toilet, rizz):
    return [f"{poo} + {pee}" for i, poo in enumerate(toilet) for pee in toilet[i:] if poo + pee == rizz]

poopee = input("Enter your list of ascending integers: ")
toilet = [int(x.strip()) for x in poopee.split(",")]
rizz = int(input("Enter your target value: "))

result = skibidi(toilet, rizz)
if skibidi(toilet, rizz):
    print(f"{result} = {rizz}")
else:
    print("Nah")