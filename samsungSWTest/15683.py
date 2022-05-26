import copy
import sys

road = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[2, 1], [1, 3], [3, 0], [0, 2]],
        [[0, 1, 2], [1, 2, 3], [0, 1, 3], [0, 2, 3]], [[0, 1, 2, 3]]]

dx = [0, 0, -1, 1] # E W N S
dy = [1, -1, 0, 0]

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
cctv = []
cnt = 0
ans = int(1e9)

for i in range(n):
    data = list(map(int, input().split()))
    arr.append(data)
    for j in range(len(data)):
        if data[j] != 0 and data[j] != 6:
            cctv.append([i, j])
            cnt += 1


def oversee(temp, number, direction):
    for d in road[number][direction]:
        x, y = dx[d], dy[d]
        while True:
            if 0 > x or n <= x or 0 > y or m <= y or temp[x][y] == 6:
                break
            if temp[x][y] == 0:
                temp[x][y] = '#'
            x += dx[d]
            y += dy[d]


def solve(temp, count):
    if count == cnt:
        global ans
        res = 0
        for a in range(n):
            for b in range(m):
                if temp[a][b] == 0:
                    res += 1
        ans = min(ans, res)
        return

    current = copy.deepcopy(temp)
    cctv_num = arr[cctv[count][0]][cctv[count][1]]
    for d in road[cctv_num]:
        oversee(current, cctv_num, d)
        solve(current, count + 1)
        current = copy.deepcopy(temp)


solve(arr, 0)
print(ans)
