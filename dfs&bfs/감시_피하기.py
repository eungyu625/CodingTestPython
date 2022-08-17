dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N = int(input())
arr = []
teacher = []
student = []
corridor = []
wall = []
answer = "NO"

for i in range(N):
    data = list(input().split())
    arr.append(data)
    for j in range(len(data)):
        if data[j] == "T":
            teacher.append([i, j])
        elif data[j] == "S":
            student.append([i, j])
        else:
            corridor.append([i, j])


def solve():
    for t in range(len(teacher)):
        tx, ty = teacher[t][0], teacher[t][1]
        d = 0
        while True:
            nx = tx + dx[d]
            ny = ty + dy[d]
            if 0 > nx or nx >= N or 0 > ny or ny >= N:
                if d == 3:
                    break
                else:
                    tx, ty = teacher[t][0], teacher[t][1]
                    d += 1
                    continue
            if arr[nx][ny] == "O":
                if d == 3:
                    break
                else:
                    tx, ty = teacher[t][0], teacher[t][1]
                    d += 1
                    continue
            if arr[nx][ny] == "S":
                return False
            tx, ty = nx, ny
    return True


def obstacle(cnt, start):
    global answer
    if cnt == 3:
        if solve():
            answer = "YES"
        return

    for c in range(start, len(corridor)):
        x, y = corridor[c]
        arr[x][y] = "O"
        obstacle(cnt + 1, c + 1)
        arr[x][y] = "X"


obstacle(0, 0)
print(answer)
