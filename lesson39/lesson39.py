# Lesson 39
def gcf_finder(num1, num2):
    f1 = [one for one in range(1, num1 + 1) if num1 % one == 0]
    f2 = [two for two in range(1, num2 + 1) if num2 % two == 0]
    return max([poop for poop in f1 if poop in f2])

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
print(gcf_finder(num1, num2))
        
