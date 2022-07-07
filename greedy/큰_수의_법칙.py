N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
arr.sort()
k = 0
for _ in range(M):
    if k == K:
        ans += arr[-2]
        k = 0
        continue
    ans += arr[-1]
    print(ans, end=' ')
    k += 1
print()
print(ans)
