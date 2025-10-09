# Lesson 30
N = int(input("Enter you number: "))
def pattern(N):
    for i in range(1, N + 1):
        monkey = ""
        for poop in range(i):
            if poop % 2 == 0:
                monkey += "1"
            else:
                monkey += "0"
        print(monkey)
pattern(N)