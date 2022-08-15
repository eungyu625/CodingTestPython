dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, K = map(int, input().split())
arr = []
virus = []

for i in range(N):
    data = list(map(int, input().split()))
    arr.append(data)
    for j in range(len(data)):
        if data[j] != 0:
            virus.append([i, j, data[j]])

S, X, Y = map(int, input().split())
virus.sort(key=lambda l: l[-1])

s = 0
while virus:
    if s == S:
        break
    x, y, k = virus.pop(0)
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == 0:
                arr[nx][ny] = k
                virus.append([nx, ny])
    s += 1

print(arr[X - 1][Y - 1])

