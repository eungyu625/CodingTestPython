dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
direction = []
snake = [[0, 0]]

for _ in range(K):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1

L = int(input())

for _ in range(L):
    direction.append(list(map(int, input().split())))

time = 1
board[0][0] = 2
tx, ty, hx, hy = 0, 0, 0, 0
d = 0

while True:
    sx = hx + dx[d]
    sy = hy + dy[d]
    if 0 > sx or sx >= N or 0 > sy or sy >= N:
        break
    if board[sx][sy] == 2:
        break
    if board[sx][sy] == 1:
        board[sx][sy] = 2
        snake.append([sx, sy])
    if board[sx][sy] == 0:
        board[sx][sy] = 2
        snake.append([sx, sy])
        board[tx][ty] = 0
        snake.pop(0)
        tx, ty = snake[0]

    if direction and time == int(direction[0][0]):
        c = direction.pop(0)[1]
        if c == "L":
            d = (d + 3) % 4
        else:
            d = (d + 1) % 4
    hx, hy = sx, sy
    time += 1

print(time)
