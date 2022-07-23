dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
fireball = []
arr = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball.append([r - 1, c - 1, m, s, d])

for _ in range(K):
    while fireball:
        r, c, m, s, d = fireball.pop(0)
        rr = (r + s * dx[d]) % N
        rc = (c + s * dy[d]) % N
        arr[rr][rc].append([m, s, d])

    for i in range(N):
        for j in range(N):
            if len(arr[i][j]) == 1:
                fireball.append([i, j] + arr[i][j].pop())
            elif len(arr[i][j]) > 1:
                sum_m, sum_s, odd, even, cnt = 0, 0, 0, 0, len(arr[i][j])
                while arr[i][j]:
                    m, s, d = arr[i][j].pop(0)
                    sum_m += m
                    sum_s += s
                    if d % 2 != 0:
                        odd += 1
                    else:
                        even += 1
                if sum_m // 5:
                    if odd == cnt or even == cnt:
                        nd = [0, 2, 4, 6]
                    else:
                        nd = [1, 3, 5, 7]

                    for d in nd:
                        fireball.append([i, j, sum_m // 5, sum_s // cnt, d])

print(sum(f[2] for f in fireball))
