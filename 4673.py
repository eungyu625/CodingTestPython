
arr = [i for i in range(1, 10000)]

for i in range(len(arr)):
    res = i + 1
    num = i + 1
    while num:
        res += num % 10
        num //= 10
    if res < 10000:
        arr[res - 1] = 0

for i in range(len(arr)):
    if arr[i] != 0:
        print(i + 1)
