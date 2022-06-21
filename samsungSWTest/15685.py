import sys

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
# 동 북 서 남, 시계 방향 : 동 -> 북 -> 서 -> 남
# 0 : x 좌표가 증가하는 방향
# 1 : y 좌표가 감소하는 방향
# 2 : x 좌표가 감소하는 방향
# 3 : y 좌표가 증가하는 방향

input = sys.stdin.readline

arr = [[0] * 101 for _ in range(101)]
ans = 0

n = int(input())
for _ in range(n):
    x, y, d, g = map(int, input().split())
    arr[y][x] = 1
    curve = [d]
    nx = x + dx[d]
    ny = y + dy[d]
    arr[ny][nx] = 1
    for i in range(1, g + 1):
        current = list(reversed(curve))
        for j in range(len(current)):
            nd = (current[j] + 1) % 4
            nx += dx[nd]
            ny += dy[nd]
            arr[ny][nx] = 1
            curve.append(nd)

for i in range(100):
    for j in range(100):
        if arr[i][j] == 1 and arr[i + 1][j] == 1 and arr[i][j + 1] == 1 and arr[i + 1][j + 1] == 1:
            ans += 1

print(ans)
