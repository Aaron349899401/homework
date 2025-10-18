# Lesson 41
def scrabble_score(string_list):
    point_list = []
    for item in string_list:
        points = 0
        for letter in item:
            if letter in {"A", "E", "I", "L", "N", "O", "R", "S", "T", "U"}:
                points += 1
            elif letter in {"D", "G"}:
                points += 2
            elif letter in {"B", "C", "M", "P"}:
                points += 3
            elif letter in {"F", "H", "V", "W", "Y"}:
                points += 4
            elif letter in {"K"}:
                points += 5
            elif letter in {"J", "X"}:
                points += 8
            elif letter in {"Q", "Z"}:
                points += 10
        point_list.append(points)
    return f"{item.lower().capitalize()}: {max(point_list)}"

string = input("Enter your list of strings: ")
string_list = [x.strip().upper() for x in string.split(",")]

print(scrabble_score(string_list))