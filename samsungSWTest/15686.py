
import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
home = []
store = []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(len(data)):
        if data[j] == 2:
            store.append([i, j])
        elif data[j] == 1:
            home.append([i, j])

ans = int(1e9)

survive = list(combinations(store, m))

for i in range(len(survive)):
    res = 0
    for [x, y] in home:
        dist = 101
        for [a, b] in survive[i]:
            dist = min(dist, abs(x - a) + abs(y - b))
        res += dist
    ans = min(res, ans)

print(ans)


