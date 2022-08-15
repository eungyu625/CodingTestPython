import copy

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
virus = []
arr = []
answer = 0

for i in range(N):
    data = list(map(int, input().split()))
    arr.append(data)
    for j in range(len(data)):
        if data[j] == 2:
            virus.append([i, j])


def solve():
    global answer
    temp = copy.deepcopy(arr)
    queue = []
    for vx, vy in virus:
        queue.append([vx, vy])

    while queue:
        x, y = queue.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    queue.append([nx, ny])

    res = 0
    for x in range(N):
        for y in range(M):
            if temp[x][y] == 0:
                res += 1
    answer = max(answer, res)


def new_wall(cnt, x, y):
    if cnt == 3:
        solve()
        return

    for a in range(N):
        for b in range(M):
            if arr[a][b] == 0:
                arr[a][b] = 1
                new_wall(cnt + 1, a, b)
                arr[a][b] = 0


new_wall(0, 0, 0)
print(answer)
