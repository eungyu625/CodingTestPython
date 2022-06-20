import sys

input = sys.stdin.readline

r, c, t = map(int, input().split())
arr = []
cleaner = []
ans = 0

for i in range(r):
    data = list(map(int, input().split()))
    arr.append(data)
    for j in range(len(data)):
        if data[j] == -1:
            cleaner.append([i, j])


def diffusion():
    current = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if arr[x][y] == -1:
                continue
            cnt = 0
            if x + 1 < r and arr[x + 1][y] != -1:
                cnt += 1
                current[x + 1][y] += arr[x][y] // 5
            if x - 1 >= 0 and arr[x - 1][y] != -1:
                cnt += 1
                current[x - 1][y] += arr[x][y] // 5
            if y + 1 < c and arr[x][y + 1] != -1:
                cnt += 1
                current[x][y + 1] += arr[x][y] // 5
            if y - 1 >= 0 and arr[x][y - 1] != -1:
                cnt += 1
                current[x][y - 1] += arr[x][y] // 5
            arr[x][y] -= (arr[x][y] // 5) * cnt

    for x in range(r):
        for y in range(c):
            arr[x][y] += current[x][y]


def air_up():
    x = cleaner[0][0]
    y = cleaner[0][1] + 1
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    check = [[0] * c for _ in range(r)]
    d = 0
    res = arr[x][y]
    arr[x][y] = 0
    check[x][y] = 1

    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 > nx or nx >= r or 0 > ny or ny >= c:
            d += 1
            continue
        if arr[nx][ny] == -1 or check[nx][ny] == 1:
            break
        arr[nx][ny], res = res, arr[nx][ny]
        check[nx][ny] = 1
        x += dx[d]
        y += dy[d]


def air_down():
    x = cleaner[1][0]
    y = cleaner[1][1] + 1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    check = [[0] * c for _ in range(r)]
    d = 0
    res = arr[x][y]
    arr[x][y] = 0
    check[x][y] = 1

    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 > nx or nx >= r or 0 > ny or ny >= c:
            d += 1
            continue
        if arr[nx][ny] == -1 or check[nx][ny] == 1:
            break
        arr[nx][ny], res = res, arr[nx][ny]
        check[nx][ny] = 1
        x += dx[d]
        y += dy[d]


for _ in range(t):
    diffusion()
    air_up()
    air_down()

for i in range(r):
    for j in range(c):
        if arr[i][j] > 0:
            ans += arr[i][j]

print(ans)
