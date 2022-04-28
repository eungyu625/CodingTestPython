
import heapq

INF = int(1e9)
n, k = map(int, input().split())
distance = [INF] * 100001


def dijkstra():
    q = []
    heapq.heappush(q, (0, n))
    distance[n] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in [now - 1, now + 1, now * 2]:
            if 0 <= i <= 100000:
                if i == now * 2 and distance[i] == INF:
                    distance[i] = dist
                    heapq.heappush(q, (dist, i))
                elif distance[i] == INF:
                    distance[i] = dist + 1
                    heapq.heappush(q, (dist + 1, i))


dijkstra()
print(distance[k])
