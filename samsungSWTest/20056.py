N, M, K = map(int, input().split())
fireballs = []

for _ in range(M):
    ri, ci, mi, si, di = map(int, input().split())
    fireballs.append([ri - 1, ci - 1, mi, si, di])

MAP = [[[] for _ in range(N)] for _ in range(N)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    while fireballs:
        cr, cc, cm, cs, cd = fireballs.pop(0)
        rr = (cr + cs * dx[cd]) % N
        rc = (cc + cs * dy[cd]) % N
        MAP[rr][rc].append([cm, cs, cd])

    for r in range(N):
        for c in range(N):
            if len(MAP[r][c]) > 1:
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(MAP[r][c])
                while MAP[r][c]:
                    _m, _s, _d = MAP[r][c].pop(0)
                    sum_m += _m
                    sum_s += _s
                    if _d % 2 == 1:
                        cnt_odd += 1
                    else:
                        cnt_even += 1
                if cnt_odd == cnt or cnt_even == cnt:
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                for d in nd:
                    fireballs.append([r, c, sum_m // 5, sum_s // cnt, d])
            if len(MAP[r][c]) == 1:
                fireballs.append([r, c] + MAP[r][c].pop())

print(sum(f[2] for f in fireballs))
