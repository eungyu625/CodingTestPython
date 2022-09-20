def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(x)
    return parent[x]


def union_parent(num1, num2):
    child_a = find_parent(num1)
    child_b = find_parent(num2)
    if child_a < child_b:
        parent[child_b] = child_a
    else:
        parent[child_a] = child_b


n, m = map(int, input().split())
parent = [0] * (n + 1)

edges = []
result = 0

for i in range(n + 1):
    parent[i] = i

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append([cost, a, b])

edges.sort()
last = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost
        last = cost

print(result - last)
