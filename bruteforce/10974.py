
n = int(input())

arr = [i for i in range(1, n + 1)]
check = [0] * 9


def solve(index, res):
    if index == n:
        for i in range(n):
            print(res[i], end=' ')
        print()
        return
    for i in range(n):
        if not check[i]:
            check[i] = True
            res.append(arr[i])
            solve(index + 1, res)
            res.pop()
            check[i] = False


solve(0, [])
