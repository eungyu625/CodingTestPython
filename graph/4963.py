
from collections import deque

dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [-1, 1, 0, 0, -1, 1, 1, -1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    arr = []
    check = [[0] * w for _ in range(h)]
    for _ in range(h):
        arr.append(list(map(int, input().split())))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and check[i][j] == 0:
                arr[i][j] = cnt
                check[i][j] = 1
                queue = deque()
                queue.append((i, j))

                while queue:
                    x, y = queue.popleft()
                    for k in range(8):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < h and 0 <= ny < w:
                            if arr[nx][ny] == 1 and check[nx][ny] == 0:
                                arr[nx][ny] = cnt
                                check[nx][ny] = 1
                                queue.append((nx, ny))

                cnt += 1

    print(cnt)
