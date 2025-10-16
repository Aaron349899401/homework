# Lesson 39
def gcf_finder(num1, num2):
    list1 = [one for one in range(1, num1 // 2 + 1) if num1 % one == 0]
    list2 = [two for two in range(1, num2 // 2 + 1) if num2 % two == 0]
    shared = [i for i in list1 if i in list2]
    return max(shared) if shared else None
    
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

result = gcf_finder(num1, num2)
print(result)

        
