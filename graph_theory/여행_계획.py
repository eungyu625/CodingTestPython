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


def check(travel):
    road = travel[0]
    for t in travel:
        if parent[road] != parent[t]:
            return False
    return True


n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

edges = []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(len(data)):
        if data[j] == 1:
            edges.append((i + 1, j + 1))

trip = list(map(int, input().split()))
edges.sort()

for edge in edges:
    a, b = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)

if check(trip):
    print("YES")
else:
    print("NO")
