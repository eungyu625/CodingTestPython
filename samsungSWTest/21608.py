N = int(input())
arr = [[0] * N for _ in range(N)]
favorite = [[] for _ in range(pow(N, 2) + 1)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for _ in range(pow(N, 2)):
    student, f1, f2, f3, f4 = map(int, input().split())
    favorite[student].append([f1, f2, f3, f4])
    check = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                likeCount = 0
                emptyCount = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] == f1 or arr[nx][ny] == f2 or arr[nx][ny] == f3 or arr[nx][ny] == f4:
                            likeCount += 1
                        if arr[nx][ny] == 0:
                            emptyCount += 1
                check.append([likeCount, emptyCount, i, j])

    check.sort(key=lambda l: (-l[0], -l[1], l[2], l[3]))
    arr[check[0][2]][check[0][3]] = student

ans = 0
for i in range(N):
    for j in range(N):
        res = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                for f in favorite[arr[i][j]]:
                    if arr[nx][ny] in f:
                        res += 1
        if res != 0:
            ans += pow(10, res - 1)

print(ans)
