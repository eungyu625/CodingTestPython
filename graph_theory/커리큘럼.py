import copy

v = int(input())
degree = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]
time = [0] * (v + 1)

for a in range(1, v + 1):
    data = list(map(int, input().split()))
    time[a] = data[0]
    for b in data[1:-1]:
        degree[a] += 1
        graph[b].append(a)


def topology_sort():
    result = copy.deepcopy(time)
    q = []

    for i in range(1, v + 1):
        if degree[i] == 0:
            q.append(i)

    while q:
        now = q.pop(0)

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            degree[i] -= 1
            if degree[i] == 0:
                q.append(i)

    for i in range(1, v + 1):
        print(result[i])


topology_sort()