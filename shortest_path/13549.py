
import heapq

INF = int(1e9)
n, k = map(int, input().split())
arr = [INF] * 100001


def dijkstra():
    if k <= n:
        arr[k] = n - k
        return

    q = []
    heapq.heappush(q, (0, n))
    arr[n] = 0
    while q:
        weight, now = heapq.heappop(q)
        for next_hop in [now - 1, now + 1, now * 2]:
            if 0 <= next_hop <= 100000:
                if next_hop == 2 * now and arr[next_hop] == INF:
                    arr[next_hop] = weight
                    heapq.heappush(q, (weight, next_hop))
                elif arr[next_hop] == INF:
                    arr[next_hop] = weight + 1
                    heapq.heappush(q, (weight + 1, next_hop))


dijkstra()
print(arr[k])
