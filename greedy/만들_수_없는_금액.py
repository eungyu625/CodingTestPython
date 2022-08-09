N = int(input())

coin = list(map(int, input().split()))
coin.sort()

ans = 1
for c in coin:
    if ans < c:
        break
    ans += c

print(ans)
