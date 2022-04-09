
n = int(input())

for i in range(1, n + 1):
    if i == n:
        print(0)
        break
    num = i
    res = i
    while num:
        res += num % 10
        num //= 10
    if res == n:
        print(i)
        break
