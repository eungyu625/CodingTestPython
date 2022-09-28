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


n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(0, n + 1):
    parent[i] = i

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union_parent(a, b)
    else:
        if parent[a] == parent[b]:
            print("YES")
        else:
            print("NO")
