# Lesson 27
import re
string = input("Enter your string: ")

find_string = re.findall(r"[a-zA-Z ]", string)
result = "".join(find_string)
better_result = re.sub(r"\s+", " ", result).strip()

print(better_result)