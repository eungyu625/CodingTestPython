import copy
import sys
from itertools import combinations
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
safe = []
virus = []
ans = 0

for i in range(n):
    data = list(map(int, input().split()))
    arr.append(data)
    for j in range(len(data)):
        if data[j] == 0:
            safe.append([i, j])
        if data[j] == 2:
            virus.append([i, j])


def dfs(current):
    global virus
    global ans
    temp = copy.deepcopy(current)
    queue = deque()
    for [x, y] in virus:
        queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                queue.append((nx, ny))

    res = 0
    for x in range(n):
        for y in range(m):
            if temp[x][y] == 0:
                res += 1
    ans = max(ans, res)


for v in list(combinations(safe, 3)):
    for [i, j] in v:
        arr[i][j] = 1
    dfs(arr)
    for [i, j] in v:
        arr[i][j] = 0

print(ans)
