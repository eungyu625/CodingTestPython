
n = int(input())

p = list(map(int, input().split()))

ans = 0
res = 0

p.sort()

for i in range(n):
    res += p[i]
    ans += res

print(ans)

'''
3 1 4 3 2

1 + (1 + 2) + (1 + 2 + 3) + (1 + 2 + 3 + 3) + (1 + 2 + 3 + 3 + 4)
1+3+6+9+13
'''