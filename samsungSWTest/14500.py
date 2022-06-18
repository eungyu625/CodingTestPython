n, m = map(int, input().split())
arr = []
check = [[0] * m for _ in range(n)]

for _ in range(n):
    arr.append(list(map(int, input().split())))

ans = 0


def first_solve():
    global ans
    for i in range(n - 3):
        for j in range(m):
            if ans < arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 3][j]:
                ans = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 3][j]

    for i in range(n):
        for j in range(m - 3):
            if ans < arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i][j + 3]:
                ans = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i][j + 3]


def second_solve():
    global ans
    for i in range(n - 1):
        for j in range(m - 1):
            if ans < arr[i][j] + arr[i + 1][j] + arr[i][j + 1] + arr[i + 1][j + 1]:
                ans = arr[i][j] + arr[i + 1][j] + arr[i][j + 1] + arr[i + 1][j + 1]


def third_solve():
    global ans
    for i in range(n):
        for j in range(m - 2):
            if i >= 1:
                if ans < arr[i][j] + arr[i - 1][j] + arr[i][j + 1] + arr[i][j + 2]:
                    ans = arr[i][j] + arr[i - 1][j] + arr[i][j + 1] + arr[i][j + 2]
                if ans < arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i - 1][j + 2]:
                    ans = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i - 1][j + 2]
            if i < n - 1:
                if ans < arr[i][j] + arr[i + 1][j] + arr[i][j + 1] + arr[i][j + 2]:
                    ans = arr[i][j] + arr[i + 1][j] + arr[i][j + 1] + arr[i][j + 2]
                if ans < arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 2]:
                    ans = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 2]

    for i in range(n - 2):
        for j in range(m):
            if j >= 1:
                if ans < arr[i][j] + arr[i][j - 1] + arr[i + 1][j] + arr[i + 2][j]:
                    ans = arr[i][j] + arr[i][j - 1] + arr[i + 1][j] + arr[i + 2][j]
                if ans < arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 2][j - 1]:
                    ans = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 2][j - 1]
            if j < m - 1:
                if ans < arr[i][j] + arr[i][j + 1] + arr[i + 1][j] + arr[i + 2][j]:
                    ans = arr[i][j] + arr[i][j + 1] + arr[i + 1][j] + arr[i + 2][j]
                if ans < arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 2][j + 1]:
                    ans = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 2][j + 1]


def forth_solve():
    global ans
    for i in range(n - 2):
        for j in range(m):
            if j < m - 1:
                if ans < arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j + 1]:
                    ans = arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j + 1]
            if j >= 1:
                if ans < arr[i][j] + arr[i + 1][j] + arr[i + 1][j - 1] + arr[i + 2][j - 1]:
                    ans = arr[i][j] + arr[i + 1][j] + arr[i + 1][j - 1] + arr[i + 2][j - 1]

    for i in range(n):
        for j in range(m - 2):
            if i < n - 1:
                if ans < arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 1][j + 2]:
                    ans = arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 1][j + 2]
            if i >= 1:
                if ans < arr[i][j] + arr[i][j + 1] + arr[i - 1][j + 1] + arr[i - 1][j + 2]:
                    ans = arr[i][j] + arr[i][j + 1] + arr[i - 1][j + 1] + arr[i - 1][j + 2]


def fifth_solve():
    global ans
    for i in range(n - 2):
        for j in range(m):
            if j < m - 1:
                if ans < arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j]:
                    ans = arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j]
            if j >= 1:
                if ans < arr[i][j] + arr[i + 1][j] + arr[i + 1][j - 1] + arr[i + 2][j]:
                    ans = arr[i][j] + arr[i + 1][j] + arr[i + 1][j - 1] + arr[i + 2][j]

    for i in range(n):
        for j in range(m - 2):
            if i < n - 1:
                if ans < arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i][j + 2]:
                    ans = arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i][j + 2]
            if i >= 1:
                if ans < arr[i][j] + arr[i][j + 1] + arr[i - 1][j + 1] + arr[i][j + 2]:
                    ans = arr[i][j] + arr[i][j + 1] + arr[i - 1][j + 1] + arr[i][j + 2]


first_solve()
second_solve()
third_solve()
forth_solve()
fifth_solve()
print(ans)