n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = []


def solution(pay, day, previous):
    if day > n:
        dp.append(pay - arr[previous][1])
        return
    if day == n:
        dp.append(pay)
        return

    solution(pay, day + 1, day)
    solution(pay + arr[day][1], day + arr[day][0], day)


solution(0, 0, 0)

result = 0

for i in range(len(dp)):
    result = max(result, dp[i])

print(result)
