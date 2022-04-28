
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())
arr = []
ans = 0

for _ in range(n):
    arr.append(list(map(int, input().split())))


def bfs():
    index = 0
    check = [[0] * m for _ in range(n)]
    queue = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0 and check[i][j] == 0:
                index += 1
                check[i][j] = 1
                queue.append((i, j))
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and check[nx][ny] == 0 and arr[nx][ny] != 0:
                            check[nx][ny] = 1
                            queue.append((nx, ny))

    return index


def solve():
    while True:
        global ans
        existence = False
        check = [[0] * m for _ in range(n)]
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if arr[i][j] != 0:
                    check[i][j] = 1
                    res = 0
                    if arr[i + 1][j] == 0 and check[i + 1][j] == 0:
                        res += 1
                    if arr[i - 1][j] == 0 and check[i - 1][j] == 0:
                        res += 1
                    if arr[i][j + 1] == 0 and check[i][j + 1] == 0:
                        res += 1
                    if arr[i][j - 1] == 0 and check[i][j - 1] == 0:
                        res += 1
                    if arr[i][j] < res:
                        arr[i][j] = 0
                    else:
                        arr[i][j] = arr[i][j] - res
                if arr[i][j] != 0:
                    existence = True

        if not existence:
            ans = 0
            break
        else:
            ans += 1
            if bfs() >= 2:
                break


solve()
print(ans)
