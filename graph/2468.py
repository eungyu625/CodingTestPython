
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n = int(input())
arr = []
ans = 0

for _ in range(n):
    arr.append(list(map(int, input().split())))


for i in range(1, 101):
    check = [[0] * n for _ in range(n)]

    for j in range(n):
        for k in range(n):
            if arr[j][k] <= i:
                check[j][k] = 1

    cnt = 0
    for j in range(n):
        for k in range(n):
            if check[j][k] == 0:
                check[j][k] = 2
                queue = deque()
                queue.append((j, k))
                while queue:
                    x, y = queue.popleft()

                    for a in range(4):
                        nx = x + dx[a]
                        ny = y + dy[a]

                        if 0 <= nx < n and 0 <= ny < n:
                            if check[nx][ny] == 0:
                                check[nx][ny] = 2
                                queue.append((nx, ny))
                cnt += 1
    if cnt == 0:
        cnt = 1

    if ans < cnt:
        ans = cnt

print(ans)
