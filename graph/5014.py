from collections import deque

f, s, g, u, d = map(int, input().split())
arr = [0] * (f + 1)
check = [0] * (f + 1)

queue = deque()
queue.append(s)
check[s] = 1

while queue:
    x = queue.popleft()
    if x + u <= f and check[x + u] == 0:
        check[x + u] = 1
        arr[x + u] = arr[x] + 1
        queue.append(x + u)
    if x - d >= 1 and check[x - d] == 0:
        check[x - d] = 1
        arr[x - d] = arr[x] + 1
        queue.append(x - d)


if check[g] != 0:
    print(arr[g])
else:
    print("use the stairs")
