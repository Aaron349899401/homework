# Lesson 40
num = int(input("Enter a number: "))
prime = []
for i in range(2, num + 1):
    poop = True
    for wow in range(2, int(i**0.5) + 1):
        if i % wow == 0:
            poop = False
            break
    if poop:
        prime.append(i)
print(prime)
        
