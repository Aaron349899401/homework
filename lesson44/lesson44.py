# Lesson 44
def dic(string):
    dict = {}
    for item in string:
        item = item.strip()
        dict[item] = dict.get(item, 0) + 1
    return dict

string = input("Enter your string: ")
result = dic(string)
# dict() prevent writing names as "dict"
for address, value in result.items():
    print(f"{address}:{value}")