
from collections import deque

dx = [0, -1, 1, 0]
dy = [1, 0, 0, -1]

n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input())))


def bfs():
    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = arr[x][y] + 1
                    queue.append((nx, ny))

    return arr[n - 1][m - 1]


print(bfs())
