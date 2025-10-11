# Lesson 33
def mean(int_list):
    return sum(int_list) / len(int_list)

def median(int_list):
    for num in int_list:
        sort_list = sorted(int_list)
        length = len(sort_list)
        if length % 2 == 0:
            poop1 = length // 2 - 1
            poop2 = length // 2 
            return (sort_list[poop1] + sort_list[poop2]) / 2
        else:
            return sort_list[length // 2]

raw_list = input("Enter your list of numbers: ")
int_list = [int(x.strip()) for x in raw_list.split(",")]

mean_result = mean(int_list)
median_result = median(int_list)

print("The mean is:", mean_result)
print("The median is:", median_result)