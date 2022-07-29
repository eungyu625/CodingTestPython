dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
ax = [-1, 1, -1, 1]
ay = [-1, -1, 1, 1]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cloud = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]
command = [list(map(int, input().split())) for _ in range(M)]

for d, s in command:
    sky = [[0] * N for _ in range(N)]
    while cloud:
        x, y = cloud.pop(0)
        nx = (x + s * dx[d - 1]) % N
        ny = (y + s * dy[d - 1]) % N
        sky[nx][ny] = 1

    for i in range(N):
        for j in range(N):
            if sky[i][j] == 1:
                arr[i][j] += 1

    for i in range(N):
        for j in range(N):
            if sky[i][j] == 1:
                for k in range(4):
                    nx = i + ax[k]
                    ny = j + ay[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] != 0:
                            arr[i][j] += 1

    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and sky[i][j] == 0:
                arr[i][j] -= 2
                cloud.append([i, j])

ans = 0
for i in range(N):
    for j in range(N):
        ans += arr[i][j]

print(ans)
