
n = int(input())
dp = list(map(int, input().split()))

for i in range(1, n):
    if dp[i] < dp[i - 1] + dp[i]:
        dp[i] = dp[i - 1] + dp[i]

ans = dp[0]
for i in range(n):
    if ans < dp[i]:
        ans = dp[i]

print(ans)
