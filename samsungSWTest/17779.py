import sys

dx = [-1, 1, 1, -1]
dy = [1, 1, -1, -1]

input = sys.stdin.readline

n = int(input())
arr = []
ans = int(1e9)

for _ in range(n):
    arr.append(list(map(int, input().split())))


def solve(x, y, d1, d2):
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    n5 = 0
    check = [[0] * n for _ in range(n)]

    for i in range(y - d1):
        for j in range(x + d1 + 1):
            check[i][j] = 1
            n1 += arr[i][j]
        for j in range(x + d1 + 1, n):
            check[i][j] = 2
            n2 += arr[i][j]

    for i in range(y + d2 + 1, n):
        for j in range(x + d2):
            check[i][j] = 3
            n3 += arr[i][j]
        for j in range(x + d2, n):
            check[i][j] = 4
            n4 += arr[i][j]

    x1 = x + d1
    for i in range(y - d1, y):
        for j in range(x1):
            check[i][j] = 1
            n1 += arr[i][j]
        x1 -= 1

    x2 = x + d1 + 1
    for i in range(y - d1, y - d1 + d2 + 1):
        for j in range(x2, n):
            check[i][j] = 2
            n2 += arr[i][j]
        x2 += 1

    x3 = x
    for i in range(y, y + d2 + 1):
        for j in range(x3):
            check[i][j] = 3
            n3 += arr[i][j]
        x3 += 1

    x4 = x + d1 + d2
    for i in range(y - d1 + d2 + 1, y + d2 + 1):
        for j in range(x4, n):
            check[i][j] = 4
            n4 += arr[i][j]
        x4 -= 1

    for i in range(n):
        for j in range(n):
            if check[i][j] == 0:
                n5 += arr[i][j]

    max_n = max(n1, n2, n3, n4, n5)
    min_n = min(n1, n2, n3, n4, n5)

    return max_n - min_n


for D1 in range(1, n):
    for D2 in range(1, n):
        if D1 + D2 == n:
            break
        for Y in range(D1, n - D2):
            for X in range(0, n - D1 - D2):
                ans = min(solve(X, Y, D1, D2), ans)


print(ans)
