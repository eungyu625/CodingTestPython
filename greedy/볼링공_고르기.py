N, M = map(int, input().split())
bowling = list(map(int, input().split()))

ans = 0

for a in range(len(bowling) - 1):
    for b in range(a + 1, len(bowling)):
        if bowling[a] != bowling[b]:
            ans += 1

print(ans)
