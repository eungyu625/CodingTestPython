from collections import deque

N, M, gas = map(int, input().split())
arr = []
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
for _ in range(N):
    arr.append(list(map(int, input().split())))

tx, ty = map(int, input().split())
taxi = [tx - 1, ty - 1]
passenger = []
for _ in range(M):
    sx, sy, ex, ey = map(int, input().split())
    passenger.append([sx - 1, sy - 1, ex - 1, ey - 1])

for p in passenger:
    distance = [[0] * N for _ in range(N)]
    queue = deque()
    sx, sy, ex, ey = p
    queue.append([sx, sy])
    while queue:
        x, y = queue.popleft()
        if x == ex and y == ey:
            break
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and distance[nx][ny] == 0:
                if nx != sx or ny != sy:
                    if arr[nx][ny] == 0:
                        distance[nx][ny] = distance[x][y] + 1
                        queue.append([nx, ny])
    if distance[ex][ey] == 0:
        print(-1)
        exit()
    p += [distance[ex][ey]]

while True:
    if not passenger:
        print(gas)
        break
    if gas == 0 and passenger:
        print(-1)
        break
    distance = [[0] * N for _ in range(N)]
    queue = deque()
    queue.append([taxi[0], taxi[1]])
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and distance[nx][ny] == 0:
                if nx != taxi[0] or ny != taxi[1]:
                    if arr[nx][ny] == 0:
                        distance[nx][ny] = distance[x][y] + 1
                        queue.append([nx, ny])
    for p in passenger:
        p += [distance[p[0]][p[1]]]
    passenger.sort(key=lambda l: (l[-1], l[0], l[1]))
    if passenger[0][-1] == 0:
        if passenger[0][0] != taxi[0] or passenger[0][1] != taxi[1]:
            print(-1)
            break
    if gas < passenger[0][-2] + passenger[0][-1]:
        print(-1)
        break
    gas -= passenger[0][-2] + passenger[0][-1]
    gas += 2 * passenger[0][-2]
    taxi = [passenger[0][2], passenger[0][3]]
    passenger.pop(0)
    for p in passenger:
        p.pop()
