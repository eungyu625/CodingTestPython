N = int(input())
arr = []

for _ in range(N):
    name, korean, english, math = input().split()
    arr.append([name, int(korean), int(english), int(math)])

arr.sort(key=lambda l: (-l[1], l[2], -l[3], l[0]))

for i in range(len(arr)):
    print(arr[i][0])
