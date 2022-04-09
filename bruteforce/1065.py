
n = int(input())
res = 0

for i in range(1, n + 1):
    num = i
    if i < 100:
        res += 1
    elif 100 <= i < 1000:
        rest1 = num % 10
        num //= 10
        rest2 = num % 10
        num //= 10
        rest3 = num % 10
        if rest1 - rest2 == rest2 - rest3:
            res += 1

print(res)
