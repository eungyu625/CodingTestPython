from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

N = int(input())
arr = []
shark = []
shark_size = 2
prey_num = 0
fish = []
ans = 0
for i in range(N):
    data = list(map(int, input().split()))
    arr.append(data)
    for j in range(len(data)):
        if 0 < data[j] < 9:
            fish.append([i, j, data[j]])
        if data[j] == 9:
            shark = [i, j]
arr[shark[0]][shark[1]] = 0

while True:
    if not fish:
        break

    distance = [[0] * N for _ in range(N)]
    queue = deque()
    queue.append([shark[0], shark[1]])
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and distance[nx][ny] == 0 and arr[nx][ny] != 9:
                if arr[nx][ny] > shark_size:
                    distance[nx][ny] = "X"
                    continue
                distance[nx][ny] = distance[x][y] + 1
                queue.append([nx, ny])

    prey = []
    for f in fish:
        if f[-1] < shark_size and distance[f[0]][f[1]] != 0:
            prey.append([f[0], f[1], distance[f[0]][f[1]], f[-1]])
    if not prey:
        break
    else:
        prey.sort(key=lambda l: (l[2], l[0], l[1]))
        p_x, p_y, p_d, p_s = prey[0]
        fish.remove([p_x, p_y, p_s])
        prey_num += 1
        if prey_num == shark_size:
            prey_num = 0
            shark_size += 1
        arr[shark[0]][shark[1]] = 0
        shark = [p_x, p_y]
        arr[p_x][p_y] = 9
        ans += p_d

print(ans)
