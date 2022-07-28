dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, Q = map(int, input().split())
N = pow(2, N)
arr = [list(map(int, input().split())) for _ in range(N)]
magic = list(map(int, input().split()))

ans = 0
max_num = -1
for m in magic:
    check = [[0] * N for _ in range(N)]

    if m > 0:
        for at in range(1, m + 1):
            L = pow(2, at - 1)
            use = [[0] * L for _ in range(L)]
            a, b = 0, 0

            while True:
                if b == N:
                    b = 0
                    a += pow(2, at)
                if a == N:
                    break

                for i in range(a, a + L):
                    for j in range(b, b + L):
                        use[i - a][j - b] = arr[i][j]

                nx, ny = a, b
                for k in range(4):
                    nx += dx[k] * L
                    ny += dy[k] * L
                    for i in range(L):
                        for j in range(L):
                            use[i][j], arr[i + nx][j + ny] = arr[i + nx][j + ny], use[i][j]

                b += pow(2, at)

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                continue
            res = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    if arr[nx][ny] != 0:
                        res += 1
            if res < 3:
                check[i][j] = 1

    for i in range(N):
        for j in range(N):
            if check[i][j] == 1:
                arr[i][j] -= 1

chunk = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0 and chunk[i][j] == 0:
            q = [(i, j)]
            res = 2
            chunk[i][j] = 1
            while q:
                x, y = q.pop(0)
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] != 0 and chunk[nx][ny] == 0:
                            chunk[nx][ny] = res
                            q.append((nx, ny))
                            res += 1

for i in range(N):
    for j in range(N):
        max_num = max(max_num, chunk[i][j])
        ans += arr[i][j]

print(ans)
print(max_num)
