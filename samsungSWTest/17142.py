import copy
from collections import deque
from itertools import combinations

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())
arr = []
virus = []
ans = int(1e9)

for i in range(n):
    data = list(map(int, input().split()))
    arr.append(data)
    for j in range(len(data)):
        if data[j] == 2:
            virus.append([i, j])


def solve(vital):
    queue = deque()
    check = [[0] * n for _ in range(n)]
    current = copy.deepcopy(arr)
    for a in vital:
        queue.append((a[0], a[1], 0))
    res = 0
    while queue:
        print(queue)
        for a in range(n):
            for b in range(n):
                print(current[a][b], end=' ')
            print()
        print("res = ", res)
        x, y, cnt = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not check[nx][ny] and current[nx][ny] != 1:
                check[nx][ny] = 1
                if current[nx][ny] == 0:
                    current[nx][ny] = 2
                    res = cnt + 1
                queue.append((nx, ny, cnt + 1))

    for a in range(n):
        for b in range(n):
            if current[a][b] == 0:
                return -1
    return res


candidates = list(combinations(virus, m))

for i in candidates:
    if solve(i) != -1:
        ans = min(ans, solve(i))

if ans == int(1e9):
    print(-1)
else:
    print(ans)
