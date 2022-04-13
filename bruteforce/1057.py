
n, kim, im = map(int, input().split())


def solve(k, i, t, ans):
    if t == 0:
        print(-1)
        return
    if (k % 2 == 0 and i == k - 1) or (i % 2 == 0 and k == i - 1):
        print(ans)
        return
    if k % 2 != 0:
        k += 1
    if i % 2 != 0:
        i += 1
    solve(k // 2, i // 2, t // 2, ans + 1)


solve(kim, im, n, 1)
