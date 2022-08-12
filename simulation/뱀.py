dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
snake = [[0, 0]]
direction = []

for _ in range(K):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1

L = int(input())

for _ in range(L):
    x, c = input().split()
    direction.append([x, c])

board[0][0] = 2
time = 1
tx, ty, hx, hy, d = 0, 0, 0, 0, 0

while True:
    sx = hx + dx[d]
    sy = hy + dy[d]
    if 0 > sx or sx >= N or 0 > sy or sy >= N:
        break
    if board[sx][sy] == 2:
        break
    if board[sx][sy] == 1:
        snake.append([sx, sy])
        board[sx][sy] = 2
    if board[sx][sy] == 0:
        snake.append([sx, sy])
        board[tx][ty] = 0
        tx, ty = snake.pop(0)

    if direction and time == int(direction[0][0]):
        c = direction.pop(0)[1]
        if c == "L":
            d = (d + 3) % 4
        else:
            d = (d + 1) % 4
    time += 1
    hx, hy = sx, sy

print(time)
