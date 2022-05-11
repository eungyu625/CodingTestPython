import sys

input = sys.stdin.readline

r, c, t = map(int, input().split())
arr = []
cleaner = []

for i in range(r):
    data = list(map(int, input().split()))
    arr.append(data)
    for j in range(len(data)):
        if data[j] == -1:
            cleaner.append([i, j])


def diffusion():
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    current = [[0] * c for _ in range(r)]

    for x in range(r):
        for y in range(c):
            if arr[x][y] != 0 and arr[x][y] != -1:
                tmp = 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                        current[nx][ny] += arr[x][y] // 5
                        tmp += arr[x][y] // 5
                arr[x][y] -= tmp

    for x in range(r):
        for y in range(c):
            arr[x][y] += current[x][y]


def air_up():
    ax = [0, -1, 0, 1]
    ay = [1, 0, -1, 0]
    x, y = cleaner[0][0], cleaner[0][1] + 1
    tmp = 0
    direction = 0
    while True:
        if x == cleaner[0][0] and y == cleaner[0][1]:
            break
        nx = x + ax[direction]
        ny = y + ay[direction]
        if 0 > nx or nx >= r or 0 > ny or ny >= c:
            direction += 1
            continue
        arr[x][y], tmp = tmp, arr[x][y]
        x = nx
        y = ny


def air_down():
    ax = [0, 1, 0, -1]
    ay = [1, 0, -1, 0]
    x, y = cleaner[1][0], cleaner[1][1] + 1
    tmp = 0
    direction = 0
    while True:
        if x == cleaner[1][0] and y == cleaner[1][1]:
            break
        nx = x + ax[direction]
        ny = y + ay[direction]
        if 0 > nx or nx >= r or 0 > ny or ny >= c:
            direction += 1
            continue
        arr[x][y], tmp = tmp, arr[x][y]
        x = nx
        y = ny


for _ in range(t):
    diffusion()
    air_up()
    air_down()

ans = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] > 0:
            ans += arr[i][j]

print(ans)
