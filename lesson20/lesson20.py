# Lesson 20
perfect = []
for num in range(1, 10001):
    factors = []
    for divisor in range(1, num // 2 + 1):
        if num % divisor == 0:
            factors.append(divisor)
    if sum(factors) == num:
        perfect.append(num)

sum = sum(perfect)
print(f"The sum of all the perfect numbers within 10,000 is {sum}!")
# rememebr that python reads your code from top to bottom, so if you perform a function on a 
# variable that is introduced after it is used, it wont work