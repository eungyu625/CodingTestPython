import heapq

INF = int(1e9)
N, M = map(int, input().split())
start = int(input())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])


def solve():
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for g in graph[now]:
            cost = dist + g[1]
            if cost < distance[g[0]]:
                distance[g[0]] = cost
                heapq.heappush(q, (cost, g[0]))


solve()
for i in range(1, N + 1):
    if distance[i] != INF:
        print(distance[i])
    else:
        print("INF")
