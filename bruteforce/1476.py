
e, s, m = map(int, input().split())

arr = [1, 1, 1]
res = 1

while True:
    if [e, s, m] == arr:
        break
    res += 1
    if arr[0] == 15:
        arr[0] = 1
    else:
        arr[0] += 1
    if arr[1] == 28:
        arr[1] = 1
    else:
        arr[1] += 1
    if arr[2] == 19:
        arr[2] = 1
    else:
        arr[2] += 1

print(res)
