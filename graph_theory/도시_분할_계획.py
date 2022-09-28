def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(x1, x2):
    child_a = find_parent(x1)
    child_b = find_parent(x2)
    if child_a < child_b:
        parent[child_b] = child_a
    else:
        parent[child_a] = child_b


n, m = map(int, input().split())
parent = [0] * (n + 1)

edges = []
result = 0

for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()
last = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost
        last = cost

print(result - last)
