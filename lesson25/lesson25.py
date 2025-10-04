# Lesson 25
numb = int(input("Enter a number: "))

def prime_factors(numb):
    largest = 0
    for wow in range(1, int(numb // 2) + 1):
        if numb % wow == 0:
            prime = True
            for i in range(2, int(wow ** 0.5) + 1):
                if wow % i == 0:
                    prime = False
                    break
            if prime:
                largest = wow
    return largest if largest > 0 else None   
lpf = prime_factors(numb)
if prime_factors(numb):
    print(f"The largest prime factor of {numb} is {lpf}")
else:
    print("No prime factors")
            
