# Lesson 36
def factors(num):
    factor_list = []
    for i in range(1, int(num // 2) + 1):
        if num % i == 0:
            factor_list.append(i)
    factor_list.append(num)
    return factor_list

def is_prime(num):
    if num < 2:
        return False
    for no in range(2, int(num ** 0.5) + 1):
        if num % no == 0:
            return False
    return True

num = int(input("Enter your number: "))
print(factors(num))
print(is_prime(num))