
n = int(input())

arr = list(map(int, input().split()))
check = [0] * (n + 1)

ans = 0


def solve(index, res):
    if index == n:
        result = 0
        for i in range(0, n - 1):
            result += abs(res[i] - res[i + 1])
        global ans
        if ans < result:
            ans = result

        return

    for i in range(n):
        if not check[i]:
            check[i] = True
            res.append(arr[i])
            solve(index + 1, res)
            check[i] = False
            res.pop()


solve(0, [])
print(ans)
