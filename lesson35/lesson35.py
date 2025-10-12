# Lesson 35
def remove_dupes(wow):
    better_wow = set(wow)
    return list(better_wow)
whoa = input("Enter your list: ")
wow = [stuff.strip() for stuff in whoa.split(",")]

print(sorted(remove_dupes(wow)))