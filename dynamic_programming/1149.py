n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[1000001] * 4 for _ in range(n + 1)]

dp[1][1] = arr[0][0]
dp[1][2] = arr[0][1]
dp[1][3] = arr[0][2]

for i in range(2, n + 1):
    dp[i][1] = min(dp[i - 1][2] + arr[i - 1][0], dp[i - 1][3] + arr[i - 1][0])
    dp[i][2] = min(dp[i - 1][1] + arr[i - 1][1], dp[i - 1][3] + arr[i - 1][1])
    dp[i][3] = min(dp[i - 1][1] + arr[i - 1][2], dp[i - 1][2] + arr[i - 1][2])

print(min(dp[n][1], dp[n][2], dp[n][3]))
