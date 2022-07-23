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
            new_sand = 0
            if z != 0:
                new_sand = int(sand[sx][sy] * z)
                total += new_sand
            else:
                new_sand = sand[sx][sy] - total

            if 0 <= nx < N and 0 <= ny < N:
                sand[nx][ny] += new_sand
            else:
                ans += new_sand


N = int(input())
sand = [list(map(int, input().split())) for _ in range(N)]
ans = 0

left = [(-1, -1, 0.1), (-1, 0, 0.07), (-1, 1, 0.01), (-2, 0, 0.02), (1, -1, 0.1), (1, 0, 0.07), (2, 0, 0.02),
        (1, 1, 0.01), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]

sx, sy = N // 2, N // 2

for i in range(1, N + 1):
    if i % 2:
        recount(i, 0, -1, left)
        recount(i, 1, 0, down)
    else:
        recount(i, 0, 1, right)
        recount(i, -1, 0, up)

print(ans)
