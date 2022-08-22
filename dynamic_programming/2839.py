n = int(input())
dp = [9999] * (n + 1)

if n < 5:
    if n == 3:
        print(1)
    else:
        print(-1)
else:
    dp[3] = 1
    dp[5] = 1
    for i in range(6, n + 1):
        dp[i] = min(dp[i - 3] + 1, dp[i - 5] + 1)

    if dp[n] == 10000:
        print(-1)
    else:
        print(dp[n])
