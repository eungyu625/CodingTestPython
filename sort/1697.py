
from collections import deque

n, k = map(int, input().split())

arr = [0] * 100000
check = [0] * 100000

queue = deque()
queue.append(n)
check[n] = 1

while queue:
    x = queue.popleft()
    if x == k:
        break

    if 0 <= x - 1:
        if check[x - 1] == 0:
            check[x - 1] = 1
            arr[x - 1] = arr[x] + 1
            queue.append(x - 1)
    if x + 1 < 100000:
        if check[x + 1] == 0:
            check[x + 1] = 1
            arr[x + 1] = arr[x] + 1
            queue.append(x + 1)
    if 2 * x < 100000:
        if check[2 * x] == 0:
            check[2 * x] = 1
            arr[2 * x] = arr[x] + 1
            queue.append(2 * x)

print(arr[k])
