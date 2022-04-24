from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

m, n = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

queue = deque()
ans = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            queue.append((i, j))  # i y축 j x축


while queue:
    y, x = queue.popleft()
    for k in range(4):
        nx = x + dx[k]  # nx y축
        ny = y + dy[k]
        if 0 <= nx < m and 0 <= ny < n and not arr[ny][nx]:
            arr[ny][nx] = arr[y][x] + 1
            queue.append((ny, nx))


for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(-1)
            exit()
        if arr[i][j] > ans:
            ans = arr[i][j]

print(ans - 1)
