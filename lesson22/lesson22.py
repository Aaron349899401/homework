# Lesson 22
Nterm = int(input("Enter a number: "))
t1 = 0
t2 = 1
if Nterm == 1:
    tN = t2
elif Nterm == 0:
    tN = t1
for i in range(3, Nterm + 1):
    tN = t1 + t2
    t1 = t2
    t2 = tN

print(f"Term number {Nterm} has a value of {tN} in the fibonacci sequence")