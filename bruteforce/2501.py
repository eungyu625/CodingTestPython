
n, k = map(int, input().split())

ans = 0

for i in range(1, n + 1):
    if n % i == 0:
        ans += 1
        if ans == k:
            print(i)
            exit()

print(0)

