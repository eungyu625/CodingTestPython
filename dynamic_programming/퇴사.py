n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

result = 0


def solution(pay, day, previous):
    global result
    if day > n:
        result = max(result, pay - arr[previous][1])
        return
    elif day == n:
        result = max(result, pay)
        return

    solution(pay, day + 1, day)
    solution(pay + arr[day][1], day + arr[day][0], day)


solution(0, 0, 0)
print(result)
