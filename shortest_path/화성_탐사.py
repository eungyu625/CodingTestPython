import heapq

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
INF = int(1e9)


def dijkstra():
    q = []
    heapq.heappush(q, (0, 0))
    distance[0][0] = graph[0][0]

    while q:
        x, y = heapq.heappop(q)

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if distance[x][y] + graph[nx][ny] < distance[nx][ny]:
                    distance[nx][ny] = distance[x][y] + graph[nx][ny]
                    heapq.heappush(q, (nx, ny))


for tc in range(int(input())):
    n = int(input())
    distance = [[INF] * n for _ in range(n)]
    graph = [[0] * n for _ in range(n)]

    for i in range(n):
        data = list(map(int, input().split()))
        for j in range(len(data)):
            graph[i][j] = data[j]

    dijkstra()
    print(distance[n - 1][n - 1])
