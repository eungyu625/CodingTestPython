N = int(input())
arr = list(map(int, input().split()))
ans = 0
arr.sort()

while arr:
    num = arr[-1]
    while num:
        arr.pop()
        num -= 1
    ans += 1

print(ans)
    