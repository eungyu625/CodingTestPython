N, M, H = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(H + 1)]
combi = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

for a in range(1, H + 1):
    for b in range(1, N):
        if graph[a][b - 1] == 0 and graph[a][b] == 0 and graph[a][b + 1] == 0:
            combi.append([a, b])


def check():
    for i in range(1, N + 1):
        now = i
        for j in range(1, H + 1):
            if graph[j][now - 1] == 1:
                now -= 1
            elif graph[j][now] == 1:
                now += 1
        if now != i:
            return False
    return True


def solve(cnt, idx):
    global ans
    if cnt >= ans:
        return
    if check():
        ans = min(ans, cnt)
        return

    for i in range(idx, len(combi)):
        x, y = combi[i]
        if graph[x][y - 1] == 0 and graph[x][y + 1] == 0:
            graph[x][y] = 1
            solve(cnt + 1, i + 1)
            graph[x][y] = 0


ans = 4
solve(0, 0)
print(ans if ans < 4 else -1)
