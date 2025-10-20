# Lesson 45
def dic(string_list):
    rizz_dict = {}
    for string in string_list:
        string = "".join(string).strip()
        rizz_dict[string] = len(string)
    return rizz_dict

def fib_dic(term_num):
    fib_dict = {}
    a, b = 0, 1
    for i in range(term_num+1):
        fib_dict[i] = a
        a, b = b, a + b
    return fib_dict

string_wow = input("Enter your list of strings: ")
string_list = string_wow.split(",")
term_num = int(input("Enter your term number: "))

result = dic(string_list)
result_fib = fib_dic(term_num)

print("\nString Length:")
for key, value in result.items():
    print(f"{key}: {value}")
print("\nFibonacci Sequence:")
for address, val in result_fib.items():
    print(f"term {address}: {val}")
