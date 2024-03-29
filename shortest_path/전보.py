import heapq

INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append([y, z])


def dijkstra():
    global c
    q = []
    heapq.heappush(q, (0, c))
    distance[c] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra()
total_city = 0
max_time = 0

for a in range(1, n + 1):
    if distance[a] < INF:
        total_city += 1
        max_time = max(max_time, distance[a])

print(total_city - 1, max_time)