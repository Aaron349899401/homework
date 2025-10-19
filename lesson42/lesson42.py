# Lesson 42
def skibidi(toilet, rizz):
    return [f"{chung} + {bun}" for i, chung in enumerate(toilet) for bun in toilet[i:] if chung + bun == rizz]

poopoo = input("Enter your list of ascending integers: ")
toilet = [int(x.strip()) for x in poopoo.split(",")]
rizz = int(input("Enter your target value: "))

result = skibidi(toilet, rizz)
if skibidi(toilet, rizz):
    print(f"{result} = {rizz}")
else:
    print("Nah")