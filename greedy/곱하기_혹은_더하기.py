S = input()
ans = int(S[0])
print(ans, end='')
for i in range(1, len(S)):
    if int(S[i - 1]) == 0 or int(S[i]) == 0:
        ans += int(S[i])
    else:
        ans *= int(S[i])

print(ans)
