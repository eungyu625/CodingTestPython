v, e = map(int, input().split())
in_degree = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1


def topology_sort():
    result = []
    q = []

    for i in range(1, v + 1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        now = q.pop(0)

        for i in graph[now]:
            in_degree[i] -= 1

            if in_degree[i] == 0:
                q.append(i)


topology_sort()
