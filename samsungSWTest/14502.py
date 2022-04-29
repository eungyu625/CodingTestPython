
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

ans = 0
n, m = map(int, input().split())
arr = []
d = [[0] * m for _ in range(n)]
check = [[0] * m for _ in range(n)]

for _ in range(n):
    arr.append(list(map(int, input().split())))


def initialize():
    for i in range(n):
        for j in range(m):
            d[i][j] = arr[i][j]


def bfs():
    queue = deque()
    for a in range(n):
        for b in range(m):
            if d[a][b] == 2:
                queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and d[nx][ny] == 0:
                d[nx][ny] = 2
                queue.append((nx, ny))

    res = 0
    for a in range(n):
        for b in range(m):
            if d[a][b] == 0:
                res += 1
    global ans
    if ans < res:
        ans = res


def solve(index):
    if index == 3:
        initialize()
        bfs()
        initialize()
        return

    for a in range(n):
        for b in range(m):
            if arr[a][b] == 0 and check[a][b] == 0:
                check[a][b] = 1
                arr[a][b] = 1
                solve(index + 1)
                arr[a][b] = 0
                check[a][b] = 0


initialize()
solve(0)
print(ans)
