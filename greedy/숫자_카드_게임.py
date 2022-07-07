N, M = map(int, input().split())
ans = -1
for _ in range(N):
    data = list(map(int, input().split()))
    res = 10001
    for j in range(len(data)):
        res = min(res, data[j])
    ans = max(res, ans)

print(ans)
