# Lesson 32
string1 = input("Enter your first string: ")
string2 = input("Enter your second string: ")
sort1 = sorted(string1)
sort2 = sorted(string2)
common_char = []
for i in sort1:
    for wow in sort2:
        if wow == i and sort1 not in common_char:
            common_char.append(wow)

print("Common Characters:", common_char)