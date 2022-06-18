import sys
import copy

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

mode = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[0, 3], [3, 1], [1, 2], [2, 0]], [[0, 1, 3], [0, 1, 2], [0, 2, 3], [1, 2, 3]], [[0, 1, 2, 3]]]

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
cctv = []
ans = int(1e9)
count = 0

for i in range(n):
    data = list(map(int, input().split()))
    arr.append(data)
    for j in range(len(data)):
        if data[j] != 0 and data[j] != 6:
            count += 1
            cctv.append([i, j])


def oversee(x, y, direction, current):
    for d in direction:
        nx = x
        ny = y
        while True:
            nx += dx[d]
            ny += dy[d]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 6:
                if arr[nx][ny] == 0:
                    current[nx][ny] = '#'
            else:
                break


def solve(cnt, current):
    if cnt == count:
        global ans
        res = 0
        for a in current:
            res += a.count(0)
        ans = min(ans, res)
        return

    temp = copy.deepcopy(current)
    x, y = cctv[cnt]
    direction = arr[x][y]
    for d in mode[direction]:
        oversee(x, y, d, temp)
        solve(cnt + 1, temp)
        temp = copy.deepcopy(current)


solve(0, arr)
print(ans)
