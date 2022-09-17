n = int(input())
dp = [0] * n

if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    dp = [0] * n
    dp[0] = 1
    dp[1] = 3

    for i in range(2, n):
        dp[i] = dp[i - 1] + 2 * dp[i - 2]
