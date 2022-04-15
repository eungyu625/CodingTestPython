
from collections import deque

dx = [0, -1, 1, 0]
dy = [1, 0, 0, -1]

n = int(input())

arr = []
ans = []
check = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(n):
    arr.append(list(map(int, input())))


for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and check[i][j] == 0:
            queue = deque()
            cnt = 1
            check[i][j] = 1
            queue.append((i, j))

            while queue:
                x, y = queue.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] == 1 and check[nx][ny] == 0:
                            check[nx][ny] = 1
                            queue.append((nx, ny))
                            cnt += 1

            ans.append(cnt)


ans.sort()
print(len(ans))

for i in range(len(ans)):
    print(ans[i])
