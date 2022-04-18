import heapq

INF = int(1e9)

n = int(input())
m = int(input())

arr = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))

first, last = map(int, input().split())


def dijkstra():
    q = []
    heapq.heappush(q, (0, first))
    distance[first] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in arr[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra()

print(distance[last])



