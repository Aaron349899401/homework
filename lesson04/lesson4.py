# Lesson 4
from math import ceil

fence1 = len(str(input()))
fence2 = len(str(input()))
fence3 = len(str(input()))

Total = fence1 + fence2 + fence3
prime = ceil(Total / 12)

print(prime)
print(Total % 12)
print(Total * 14.95)