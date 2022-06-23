import sys

input = sys.stdin.readline

dx = [-1, 0, 0, -1, 1]
dy = [-1, 1, -1, 0, 0]

n, m, x, y, k = map(int, input().split())
arr = []
dice = [0, 0, 0, 0, 0, 0]
top = 5
bottom = 0

for _ in range(n):
    arr.append(list(map(int, input().split())))

order = list(map(int, input().split()))

for i in range(k):
    nx = x + dx[order[i]]
    ny = y + dy[order[i]]
    if nx >= n or nx < 0 or ny >= m or ny < 0:
        continue
    if order[i] == 1:
        dice[0], dice[3], dice[5], dice[2] = dice[3], dice[5], dice[2], dice[0]
    elif order[i] == 2:
        dice[0], dice[3], dice[5], dice[2] = dice[2], dice[0], dice[3], dice[5]
    elif order[i] == 3:
        dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]
    else:
        dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]
    if arr[nx][ny] != 0:
        dice[bottom] = arr[nx][ny]
        arr[nx][ny] = 0
    else:
        arr[nx][ny] = dice[bottom]
    print(dice[top])
    x = nx
    y = ny
