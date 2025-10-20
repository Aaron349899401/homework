# Lesson 45
def dic(string_list):
    rizz_dict = {}
    for string in string_list:
        string = "".join(string).strip()
        rizz_dict[string] = len(string)
    return rizz_dict

def fib_dic(term_num):
    fib_dict = {}
    for i in range(1, term_num+1):
        if term_num == 0:
            value = "0"
        elif term_num == 1:
            value = "1"
        elif term_num > 1:
            value = value[i-2] + value[i-1]
        fib_dict[i] = value
    return fib_dict

string_wow = input("Enter your list of strings: ")
term_num = int(input("Enter your term number: "))

string_list = string_wow.split(",")
result = dic(string_list)
result_fib = fib_dic(term_num)
for key, value in result.items():
    print(f"{key}:{value}")
for address, val in result_fib.items():
    print(f"{address}:{val}")
