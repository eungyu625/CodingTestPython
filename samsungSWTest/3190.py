import sys

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
# 동 북 서 남

input = sys.stdin.readline

N = int(input())
check = [[0] * N for _ in range(N)]
check[0][0] = 1
K = int(input())
for _ in range(K):
    X, Y = map(int, input().split())
    check[X - 1][Y - 1] = 2

L = int(input())
direction = []
for _ in range(L):
    X, C = input().split()
    direction.append([int(X), C])


def solve():
    t = 0
    snake = []
    x = 0
    y = 0
    snake.append([x, y])
    tx = x
    ty = y
    d = 0
    while True:
        if direction and t == direction[0][0]:
            if direction[0][1] == 'L':
                d = (d + 1) % 4
            else:
                d = (d + 3) % 4
            del direction[0]
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 > nx or nx >= N or 0 > ny or ny >= N:
            t += 1
            break
        if check[nx][ny] == 0:
            t += 1
            check[tx][ty] = 0
            check[nx][ny] = 1
            snake.append([nx, ny])
            del snake[0]
            tx, ty = snake[0]
            x = nx
            y = ny
            continue
        if check[nx][ny] == 1:
            t += 1
            break
        if check[nx][ny] == 2:
            t += 1
            check[nx][ny] = 1
            snake.append([nx, ny])
            x = nx
            y = ny
    return t


print(solve())
