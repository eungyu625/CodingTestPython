N, M, H = map(int, input().split())
arr = [[0] * (N + 1) for _ in range(H + 1)]
combi = []
ans = 4

for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1

for i in range(1, H + 1):
    for j in range(1, N):
        if arr[i][j - 1] == 0 and arr[i][j] == 0 and arr[i][j + 1] == 0:
            combi.append([i, j])


def check():
    for x in range(1, N + 1):
        now = x
        for y in range(1, H + 1):
            if arr[y][now] == 1:
                now += 1
            elif arr[y][now - 1] == 1:
                now -= 1
        if now != x:
            return False
    return True


def solve(cnt, idx):
    global ans
    if cnt >= 4:
        return
    if check():
        ans = min(cnt, ans)
        return

    for x in range(idx, len(combi)):
        q, p = combi[x]
        if arr[q][p - 1] == 0 and arr[q][p + 1] == 0:
            arr[q][p] = 1
            solve(cnt + 1, x + 1)
            arr[q][p] = 0


solve(0, 0)
print(ans if ans < 4 else -1)
