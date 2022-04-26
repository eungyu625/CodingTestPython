
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

chicken = 0
house = 0
queue = deque()

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chicken += 1
            queue.append((i, j))
        if arr[i][j] == 1:
            house += 1

ans = [[] * chicken for _ in range(chicken)]
check = [0] * chicken

res = 0
while queue:
    x, y = queue.popleft()
    for a in range(n):
        for b in range(n):
            if arr[a][b] == 1:
                dist = abs(x - a) + abs(y - b)
                ans[res].append(dist)
    res += 1

result = 2500


def distance(index, city, mid):
    if index == house:
        global result
        result = min(result, mid)
        return

    min_num = 50
    for c in range(len(city)):
        min_num = min(min_num, city[c][index])
    distance(index + 1, city, mid + min_num)


def solve(index, start, city):
    if index == m:
        distance(0, city, 0)
        return

    for c in range(start, len(ans)):
        if check[c] == 0:
            check[c] = 1
            city.append(ans[c])
            solve(index + 1, c + 1, city)
            city.pop()
            check[c] = 0


solve(0, 0, [])
print(result)
