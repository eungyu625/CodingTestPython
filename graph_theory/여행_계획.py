def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(x1, x2):
    child_x1 = find_parent(x1)
    child_x2 = find_parent(x2)
    if child_x1 < child_x2:
        parent[child_x2] = child_x1
    else:
        parent[child_x1] = child_x2


def check():
    std = plans[0]

    for plan in plans:
        if find_parent(plan) != find_parent(std):
            return False
    return True


n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(len(data)):
        if data[j] == 1:
            union_parent(i + 1, j + 1)

plans = list(map(int, input().split()))

if check():
    print("YES")
else:
    print("NO")