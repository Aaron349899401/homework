# Lesson 5

money = float(input("how much money do you have?: "))
cookies = input("")
money_left = money - (cookies.count("b")*2 + cookies.count("c")*1.25)

print(len(cookies))
print((cookies.count("b")*2 + cookies.count("c")*1.25) - (cookies.count("b")*0.75 + cookies.count("c")*0.5))
print(f"You have {round(money_left, 2)} dollars left")
