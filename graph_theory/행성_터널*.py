def find_parent(x1):
    if parent[x1] != x1:
        parent[x1] = find_parent(parent[x1])
    return parent[x1]


def union_parent(x1, x2):
    child_x1 = find_parent(x1)
    child_x2 = find_parent(x2)
    if child_x1 < child_x2:
        parent[child_x2] = child_x1
    else:
        parent[child_x2] = child_x1


n = int(input())
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

x = []
y = []
z = []

for i in range(n):
    data = list(map(int, input().split()))
    x.append((data[0], i + 1))
    y.append((data[1], i + 1))
    z.append((data[2], i + 1))

edges = []
result = 0

x.sort()
y.sort()
z.sort()

for i in range(n - 1):
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost

print(result)
