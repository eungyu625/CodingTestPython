import copy

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
mode = [[], [[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 3], [2, 3], [1, 2], [0, 1]],
        [[0, 1, 3], [0, 2, 3], [1, 2, 3], [0, 1, 2]], [[0, 1, 2, 3]]]


def oversee(y, x, direction, temp):
    for d in direction:
        nx = x
        ny = y
        while True:
            nx += dx[d]
            ny += dy[d]
            if 0 <= nx < m and 0 <= ny < n and arr[ny][nx] != 6:
                if arr[ny][nx] == 0:
                    temp[ny][nx] = '#'
            else:
                break


def solve(current, cnt):
    global ans
    temp = copy.deepcopy(current)
    if cnt == cctv:
        res = 0
        for a in current:
            res += a.count(0)
        ans = min(ans, res)
        return
    y, x, direction = q[cnt]
    for a in mode[direction]:
        oversee(y, x, a, temp)
        solve(temp, cnt + 1)
        temp = copy.deepcopy(current)


n, m = map(int, input().split())
arr = []
q = []
ans = n * m
cctv = 0
for i in range(n):
    data = list(map(int, input().split()))
    arr.append(data)
    for j in range(len(data)):
        if data[j] != 0 and data[j] != 6:
            cctv += 1
            q.append([i, j, data[j]])

solve(arr, 0)
print(ans)
