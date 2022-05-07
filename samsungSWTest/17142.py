
n, m = map(int, input().split())
arr = []
virus = []

for i in range(n):
    data = list(map(int, input().split()))
    arr.append(data)
    for j in range(len(data)):
        if data[j] == 2:
            virus.append([i, j])

