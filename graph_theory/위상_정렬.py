v, e = map(int, input().split())
degree = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1


def topology_sort():
    result = []
    q = []

    for i in range(1, v + 1):
        if degree[i] == 0:
            q.append(i)

    while q:
        now = q.pop(0)
        result.append(now)

        for i in graph[now]:
            degree[i] -= 1
            if degree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')


topology_sort()
