X = int(input())
dp = [0] * (X + 1)

for i in range(X, 0, -1):
    if i % 5 == 0 and dp[int(i / 5)] == 0:
        dp[int(i / 5)] = dp[i] + 1
    if i % 3 == 0 and dp[int(i / 3)] == 0:
        dp[int(i / 3)] = dp[i] + 1
    if i % 2 == 0 and dp[int(i / 2)] == 0:
        dp[int(i / 2)] = dp[i] + 1
    if dp[i - 1] == 0:
        dp[i - 1] = dp[i] + 1

print(dp[1])
