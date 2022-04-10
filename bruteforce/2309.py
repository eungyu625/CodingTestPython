
import sys

height = list()
_sum = 0

for i in range(9):
    num = int(input())
    _sum += num
    height.append(num)

height.sort()

fir = 0
sec = 0

for i in range(8):
    for j in range(i + 1, 9):
        if _sum - (height[i] + height[j]) == 100:
            for k in range(9):
                if k != i and k != j:
                    print(height[k])
            exit()
