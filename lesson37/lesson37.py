# Lesson 37
def skibidi(rizz):
    if not rizz:
        return rizz
    comp = []
    count = 1
    for i in range(1, len(rizz)):
        if rizz[i] == rizz[i-1]:
            count += 1
        else:
            comp.append(rizz[i-1] + str(count))
            count = 1
    comp.append(rizz[-1] + str(count))
    comp_str = "".join(comp)
    return comp_str if len(comp_str) < len(rizz) else rizz

rizz = input("Enter your string: ")
result = skibidi(rizz)
print(result)