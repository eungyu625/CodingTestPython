dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

N, M, K = map(int, input().split())
arr = []
use = [[5] * N for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]
dead = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(N):
    arr.append(list(map(int, input().split())))

for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1].append(z)

for _ in range(K):

    for i in range(N):
        for j in range(N):
            tree[i][j].sort()
            length = len(tree[i][j])
            for k in range(length):
                if use[i][j] >= tree[i][j][k]:
                    use[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                else:
                    for _ in range(k, length):
                        dead[i][j].append(tree[i][j].pop())
                    break

    for i in range(N):
        for j in range(N):
            while dead[i][j]:
                use[i][j] += dead[i][j].pop() // 2

    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])):
                if tree[i][j][k] % 5 != 0:
                    continue
                for n in range(8):
                    nx = i + dx[n]
                    ny = j + dy[n]
                    if 0 <= nx < N and 0 <= ny < N:
                        tree[nx][ny].append(1)

    for i in range(N):
        for j in range(N):
            use[i][j] += arr[i][j]

ans = 0
for i in range(N):
    for j in range(N):
        ans += len(tree[i][j])

print(ans)
