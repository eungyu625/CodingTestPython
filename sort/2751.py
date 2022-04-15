n = int(input())

arr = list()

for i in range(n):
    num = int(input())
    arr.append(num)

arr.sort()

for i in range(n):
    print(arr[i])