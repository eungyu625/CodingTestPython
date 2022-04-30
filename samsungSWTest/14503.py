
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())

arr = []
check = [[0] * m for _ in range(n)]

for _ in range(n):
    arr.append(list(map(int, input().split())))

check[r][c] = 1
ans = 1

while True:
    found = False
    for _ in range(4):
        nd = (d + 3) % 4
        nx = r + dx[nd]
        ny = c + dy[nd]
        d = nd
        if 0 <= nx < m and 0 <= ny < n:
            if arr[nx][ny] == 0 and check[nx][ny] == 0:
                check[nx][ny] = 1
                ans += 1
                r = nx
                c = ny
                found = True
                break
    if not found:
        if arr[r - dx[d]][c - dy[d]] != 0:
            print(ans)
            break
        else:
            r, c = r - dx[d], c - dy[d]

