N, M = map(int, input().split())
arr = []
chicken = []
house = []
ans = int(1e9)

for i in range(N):
    data = list(map(int, input().split()))
    arr.append(data)
    for j in range(len(data)):
        if data[j] == 1:
            house.append([i, j])
        if data[j] == 2:
            chicken.append([i, j])


def solve(temp):
    global ans
    res = 0
    for hx, hy in house:
        cur = int(1e9)
        for tx, ty in temp:
            cur = min(cur, abs(hx - tx) + abs(hy - ty))
        res += cur
    ans = min(res, ans)


def combi(cnt, start, temp):
    if cnt == M:
        solve(temp)
        return

    for c in range(start, len(chicken)):
        temp.append(chicken[c])
        combi(cnt + 1, c + 1, temp)
        temp.pop()


combi(0, 0, [])
print(ans)
