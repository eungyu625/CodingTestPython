
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

m, n, k = map(int, input().split())

arr = [[0] * n for _ in range(m)]
check = [[0] * n for _ in range(m)]
queue = deque()

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for j in range(y1, y2):
        for k in range(x1, x2):
            arr[j][k] = 1

ans = 0
many = []
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0 and check[i][j] == 0:
            check[i][j] = 1
            cnt = 1
            queue.append((i, j))
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < m and 0 <= ny < n:
                        if arr[nx][ny] == 0 and check[nx][ny] == 0:
                            check[nx][ny] = 1
                            queue.append((nx, ny))
                            cnt += 1

            many.append(cnt)
            ans += 1

many.sort()

print(ans)
for i in range(len(many)):
    print(many[i], end=' ')
