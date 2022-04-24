
n = int(input())

arr = [[] * n for _ in range(n)]
check = [0] * n
route = [] * n

for i in range(n):
    route.append(list(map(int, input().split())))

ans = 10000000

for i in range(n):
    for j in range(n):
        arr[i].append(route[i][j])


def solve(city, index, res):
    if index == n - 1:
        global ans
        if arr[city][0] == 0:
            return
        if ans > res + arr[city][0]:
            ans = res + arr[city][0]

    for j in range(1, n):
        if arr[city][j] != 0 and check[j] == 0 and ans > res + arr[city][j]:
            check[j] = 1
            solve(j, index + 1, res + arr[city][j])
            check[j] = 0


solve(0, 0, 0)
print(ans)
