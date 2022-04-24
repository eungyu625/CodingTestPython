
n = int(input())
if 1 < n <= 3:
    print(1)
elif n == 1:
    print(0)
else:
    dp = [0] * (n + 1)
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1

    if n > 3:
        for i in range(4, n + 1):
            num1 = int(1e9)
            num2 = int(1e9)
            num3 = int(1e9)
            if i % 3 == 0:
                num1 = dp[i // 3] + 1
            if i % 2 == 0:
                num2 = dp[i // 2] + 1
            num3 = dp[i - 1] + 1
            dp[i] = min(num1, num2, num3)

    print(dp[n])
