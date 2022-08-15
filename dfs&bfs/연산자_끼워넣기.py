N = int(input())
arr = list(map(int, input().split()))
pl, mi, mul, div = map(int, input().split())
max_num = -int(1e9)
min_num = int(1e9)


def solve(cnt, start, current, plus, minus, multiple, divide):
    global max_num, min_num
    if cnt == len(arr):
        max_num = max(max_num, current)
        min_num = min(min_num, current)
        return

    for n in range(start, len(arr)):
        if plus > 0:
            solve(cnt + 1, n + 1, current + arr[n], plus - 1, minus, multiple, divide)
        if minus > 0:
            solve(cnt + 1, n + 1, current - arr[n], plus, minus - 1, multiple, divide)
        if multiple > 0:
            solve(cnt + 1, n + 1, current * arr[n], plus, minus, multiple - 1, divide)
        if divide > 0:
            if current < 0:
                solve(cnt + 1, n + 1, -(abs(current) // arr[n]), plus, minus, multiple, divide - 1)
            else:
                solve(cnt + 1, n + 1, current // arr[n], plus, minus, multiple, divide - 1)


solve(1, 1, arr[0], pl, mi, mul, div)
print(max_num)
print(min_num)
