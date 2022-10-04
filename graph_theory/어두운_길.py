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
parent = [0] * n

for i in range(n):
    parent[i] = i

edges = []
initial_cost = 0
min_cost = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    initial_cost += cost
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        min_cost += cost

print(initial_cost - min_cost)
