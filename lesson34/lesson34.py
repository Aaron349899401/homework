# Lesson 34
from random import randrange

def amogus(string):
    return [int(x.strip()) for x in string.split(",")]
    
def random_int(start, end, frequency):
    return [randrange(start, end + 1) for _ in range(frequency)]

print(amogus("1, 2, 3, 6, 7"))
print(random_int(1, 1000, 20))