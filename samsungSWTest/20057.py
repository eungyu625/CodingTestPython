def recount(time, x, y, direction):
    global ans, sx, sy

    for _ in range(time):
        sx += x
        sy += y
        if sy < 0:
            break

        total = 0
        for dx, dy, z in direction:
            nx = sx + dx
            ny = sy + dy
            if z != 0:
                new_sand = int(arr[sx][sy] * z)
                total += new_sand
            else:
                new_sand = arr[sx][sy] - total

            if 0 <= nx < N and 0 <= ny < N:
                arr[nx][ny] += new_sand
            else:
                ans += new_sand

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

left = [(0, -2, 0.05), (-1, -1, 0.1), (1, -1, 0.1), (-1, 0, 0.07), (1, 0, 0.07), (-1, 1, 0.01), (1, 1, 0.01),
        (-2, 0, 0.02), (2, 0, 0.02), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]

ans = 0
sx, sy = N // 2, N // 2

for i in range(1, N + 1):
    if i % 2:
        recount(i, 0, -1, left)
        recount(i, 1, 0, down)
    else:
        recount(i, 0, 1, right)
        recount(i, -1, 0, up)

print(ans)
