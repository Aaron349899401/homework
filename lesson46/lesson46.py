# Lesson 46
def collatz():
    cache = {}
    max_num = 0
    max_length = 0
    for num in range(1, 1000000):
        length = 0
        amongus = num
        while num > 1:
            if num in cache:
                length += cache[num]
                break
            if num % 2 == 0:
                num = num // 2
            else:
                num = num * 3 + 1
            length += 1
        cache[amongus] = length
        if length > max_length:
            max_length = length
            max_num = amongus
    print(f"The largest possible length is {max_length} from the {max_num}") 

collatz()