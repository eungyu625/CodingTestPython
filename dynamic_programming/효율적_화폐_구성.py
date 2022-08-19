n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(arr[i], m + 1):
        if d[j - arr[j]] != 10001:
            d[j] = min(d[j], d[j - arr[i]] + 1)