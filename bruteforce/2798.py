n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0

for i in range(n - 2):
    res = arr[i]
    for j in range(i + 1, n - 1):
        res += arr[j]
        for k in range(j + 1, n):
            res += arr[k]
            if ans < res <= m:
                ans = res
            res -= arr[k]
        res -= arr[j]
print(ans)