
from collections import deque

tc = int(input())

while tc:
    n = int(input())
    queue = deque()
    check = []
    sx, sy = map(int, input().split())
    queue.append((sx, sy))
    check.append([sx, sy])
    store = []
    for _ in range(n):
        x, y = map(int, input().split())
        store.append([x, y])
    ex, ey = map(int, input().split())
    store.append([ex, ey])

    existence = False
    while queue:
        x, y = queue.popleft()
        if x == ex and y == ey:
            print("happy")
            existence = True
            break
        for nx, ny in store:
            if [nx, ny] not in check:
                if 1000 >= abs(nx - x) + abs(ny - y):
                    queue.append((nx, ny))
                    check.append([nx, ny])

    if not existence:
        print("sad")
    tc -= 1
