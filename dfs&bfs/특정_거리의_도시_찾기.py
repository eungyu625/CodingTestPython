N, M, K, X = map(int, input().split())
arr = [0] * (N + 1)
road = [list(map(int, input().split())) for _ in range(M)]
queue = [X]

while queue:
    k = queue.pop(0)
    for x, y in road:
        if x == k and arr[y] == 0:
            arr[y] = arr[x] + 1
            queue.append(y)

answer = []
for i in range(len(arr)):
    if arr[i] == K:
        answer.append(i)

if not answer:
    print(-1)
for a in answer:
    print(a)
