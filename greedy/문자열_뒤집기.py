S = input()
first = S[0]
zero = 0
one = 0

if int(first) == 1:
    one += 1
else:
    zero += 1

for s in S:
    if s != first:
        first = s
        if int(s) == 1:
            one += 1
        else:
            zero += 1

print(min(one, zero))
