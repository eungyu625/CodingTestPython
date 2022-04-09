n = int(input())
arr = list()

for i in range(n):
    arr.append(list(map(int, input().split())))

res = [1] * n

for i in range(n - 1):
    std_weight = arr[i][0]
    std_height = arr[i][1]
    for j in range(i + 1, n):
        comp_weight = arr[j][0]
        comp_height = arr[j][1]
        if std_weight > comp_weight and std_height > comp_height:
            res[j] += 1
        elif std_weight < comp_weight and std_height < comp_height:
            res[i] += 1

for i in range(n):
    print(res[i], end=' ')
