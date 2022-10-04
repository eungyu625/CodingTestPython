for tc in range(int(input())):
    n = int(input())
    in_degree = [0] * (n + 1)
    graph = [[False] * (n + 1) for _ in range(n + 1)]

    data = list(map(int, input().split()))

    for i in range(n):
        for j in range(i + 1, n):
            graph[data[i]][data[j]] = True
            in_degree[data[j]] += 1

    m = int(input())

    for _ in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            in_degree[a] += 1
            in_degree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            in_degree[a] -= 1
            in_degree[b] += 1

    result = []
    q = []

    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)
    certain = True
    cycle = False

    for _ in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            certain = False
            break

        now = q.pop(0)
        result.append(now)

        for i in range(1, n + 1):
            if graph[now][i]:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    q.append(j)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for res in result:
            print(res, end=' ')
        print()

