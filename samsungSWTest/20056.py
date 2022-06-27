N, M, K = map(int, input().split())
fireballs = []
for _ in range(M):
    fireballs.append(list(map(int, input().split())))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

map = [[[] for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(K):
    while fireballs:
        r, c, m, s, d = fireballs.pop(0)
        nr = (r + s * dx[d]) % N
        nc = (c + s * dy[d]) % N
        map[nr][nc].append([m, s, d])

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if len(map[i][j]) > 1:
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(map[i][j])
                while map[i][j]:
                    _m, _s, _d = map[i][j].pop(0)
                    sum_m += _m
                    sum_s += _s
                    if _d % 2:
                        cnt_odd += 1
                    else:
                        cnt_even += 1
                if cnt_odd == cnt or cnt_even == cnt:
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                if sum_m // 5:
                    for k in nd:
                        fireballs.append([i, j, sum_m // 5, sum_s // cnt, k])
            if len(map[i][j]) == 1:
                fireballs.append([r, c] + map[r][c].pop())

print(sum([f[2] for f in fireballs]))
