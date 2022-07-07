N, K = map(int, input().split())
ans = 0

while True:
    if N == 1:
        print(ans)
        break
    if N % K == 0:
        N /= K
        ans += 1
    else:
        N -= 1
        ans += 1
