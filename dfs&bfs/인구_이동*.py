N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def solve(x, y, idx):
    united = [[x, y]]
    queue = [[x, y]]
    summary = arr[x][y]
    union[x][y] = idx
    while queue:
        ax, ay = queue.pop(0)
        for k in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]
            if 0 <= nx < N and 0 <= ny < N and union[nx][ny] == -1:
                union[nx][ny] = idx
                queue.append([nx, ny])
                united.append([nx, ny])
                summary += arr[nx][ny]

    summary //= len(united)
    for ux, uy in united:
        arr[ux][uy] += summary


while True:
    union = [[-1] * N in range(N)]
    index = 0
    for i in range(N):
        for j in range(N):
            if union[i][j] == -1:
                solve(i, j, index)
                index += 1
    if index == N * N:
        break
    answer += 1

print(answer)
