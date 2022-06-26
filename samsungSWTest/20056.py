import copy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# 0 1 2 3 4 5 6 7

n, m, k = map(int, input().split())
fireball = []
arr = [[0] * n for _ in range(n)]
ans = 0

for _ in range(m):
    ri, ci, mi, si, di = map(int, input().split())
    fireball.append([ri, ci, mi, si, di])
    arr[ri - 1][ci - 1] = mi

for ii in range(n):
    for jj in range(n):
        print(arr[ii][jj], end=' ')
    print()
print()


def divide():
    global fireball
    res = []
    while fireball:
        current = [fireball[0]]
        x = fireball[0][0]
        y = fireball[0][1]
        for fire in range(1, len(fireball)):
            if x == fireball[fire][0] and y == fireball[fire][1]:
                current.append(fireball[fire])
        if len(current) == 1:
            continue
        for cur in current:
            fireball.remove(cur)
        mass = 0
        velocity = 0
        val = current[0][4] % 2
        direction = True
        for cur in current:
            mass += cur[2]
            velocity += cur[3]
            if cur[4] % 2 != val:
                direction = False
        mass //= 5
        velocity //= len(current)
        if mass == 0:
            continue

        if direction:
            res.append([x, y, mass, velocity, 0])
            res.append([x, y, mass, velocity, 2])
            res.append([x, y, mass, velocity, 4])
            res.append([x, y, mass, velocity, 6])
        else:
            res.append([x, y, mass, velocity, 1])
            res.append([x, y, mass, velocity, 3])
            res.append([x, y, mass, velocity, 5])
            res.append([x, y, mass, velocity, 7])

    for value in res:
        fireball.append(value)


def move():

    for ball in fireball:
        if ball[4] == 0:
            if ball[0] + ball[3] * dx[ball[4]] < 1:
                ball[0] = n + 1 + ball[3] * dx[ball[4]]
            else:
                ball[0] += ball[3] * dx[ball[4]]
        elif ball[4] == 1:
            if ball[0] + ball[3] * dx[ball[4]] < 1 and ball[1] + ball[3] * dy[ball[4]] > n:
                ball[0] = n + 1 + ball[3] * dx[ball[4]]
                ball[1] = ball[1] + ball[3] * dy[ball[4]] - n
            else:
                if ball[0] + ball[3] * dx[ball[4]] < 1:
                    ball[0] = n + 1 + ball[3] * dx[ball[4]]
                    ball[1] += ball[3] * dy[ball[4]]
                elif ball[1] + ball[3] * dy[ball[4]] > n:
                    ball[0] += ball[3] * dx[ball[4]]
                    ball[1] = ball[1] + ball[3] * dy[ball[4]] - n
                else:
                    ball[0] += ball[3] * dx[ball[4]]
                    ball[1] += ball[3] * dy[ball[4]]
        elif ball[4] == 2:
            if ball[1] + ball[3] * dy[ball[4]] > n:
                ball[1] = ball[1] + ball[3] * dy[ball[4]] - n
            else:
                ball[1] += ball[3] * dy[ball[4]]
        elif ball[4] == 3:
            if ball[0] + ball[3] * dx[ball[4]] > n and ball[1] + ball[3] * dy[ball[4]] > n:
                ball[0] = ball[0] + ball[3] * dx[ball[4]] - n
                ball[1] = ball[1] + ball[3] * dy[ball[4]] - n
            else:
                if ball[0] + ball[3] * dx[ball[4]] > n:
                    ball[0] = ball[0] + ball[3] * dx[ball[4]] - n
                    ball[1] += ball[3] * dy[ball[4]]
                elif ball[1] + ball[3] * dy[ball[4]] > n:
                    ball[0] += ball[3] * dx[ball[4]]
                    ball[1] = ball[1] + ball[3] * dy[ball[4]] - n
                else:
                    ball[0] += ball[3] * dx[ball[4]]
                    ball[1] += ball[3] * dy[ball[4]]
        elif ball[4] == 4:
            if ball[0] + ball[3] * dx[ball[4]] > n:
                ball[0] = ball[0] + ball[3] * dx[ball[4]] - n
            else:
                ball[0] += ball[3] * dx[ball[4]]
        elif ball[4] == 5:
            if ball[0] + ball[3] * dx[ball[4]] > n and ball[1] + ball[3] * dy[ball[4]] < 1:
                ball[0] = ball[0] + ball[3] * dx[ball[4]] - n
                ball[1] = n + 1 + ball[3] * dy[ball[4]]
            else:
                if ball[0] + ball[3] * dx[ball[4]] > n:
                    ball[0] = ball[0] + ball[3] * dx[ball[4]] - n
                    ball[1] += ball[3] * dy[ball[4]]
                elif ball[1] + ball[3] * dy[ball[4]] < 1:
                    ball[0] += ball[3] * dx[ball[4]]
                    ball[1] = n + 1 + ball[3] * dy[ball[4]]
                else:
                    ball[0] += ball[3] * dx[ball[4]]
                    ball[1] += ball[3] * dy[ball[4]]
        elif ball[4] == 6:
            if ball[1] + ball[3] * dy[ball[4]] < 1:
                ball[1] = n + 1 + ball[3] * dy[ball[4]]
            else:
                ball[1] += ball[3] * dy[ball[4]]
        elif ball[4] == 7:
            if ball[0] + ball[3] * dx[ball[4]] < 1 and ball[0] + ball[3] * dy[ball[4]] < 1:
                ball[0] = n + 1 + ball[3] * dx[ball[4]]
                ball[1] = n + 1 + ball[3] * dy[ball[4]]
            else:
                if ball[0] + ball[3] * dx[ball[4]] < 1:
                    ball[0] = n + 1 + ball[3] * dx[ball[4]]
                    ball[1] += ball[3] * dy[ball[4]]
                elif ball[1] + ball[3] * dy[ball[4]] < 1:
                    ball[0] += ball[3] * dx[ball[4]]
                    ball[1] = n + 1 + ball[3] * dy[ball[4]]
                else:
                    ball[0] += ball[3] * dx[ball[4]]
                    ball[1] += ball[3] * dy[ball[4]]
    current = [[0] * n for _ in range(n)]
    for p in range(n):
        for q in range(n):
            for ball in fireball:
                if p == ball[0] - 1 and q == ball[1] - 1:
                    current[p][q] += ball[2]


for i in range(k):
    move()
    divide()
    temp = [[0] * n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for fb in fireball:
                if a == fb[0] - 1 and b == fb[1] - 1:
                    temp[a][b] += fb[2]
    for a in range(n):
        for b in range(n):
            print(temp[a][b], end=' ')
        print()
    print()

for fb in fireball:
    ans += fb[2]

print(ans)
