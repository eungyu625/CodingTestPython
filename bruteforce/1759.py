
l, c = map(int, input().split())
arr = list(map(str, input().split()))
check = [0] * c
arr.sort()
ans = []

def vowel_consonant(res):
    vowel = 0
    consonant = 0
    for i in range(len(res)):
        if res[i] in 'aeiou':
            vowel += 1
        else:
            consonant += 1

    if vowel >= 1 and consonant >= 2:
        ans.append(res)


def solve(index, res, start):
    if index == l:
        vowel_consonant(res)

    for i in range(start, c):
        if check[i] == 0:
            check[i] = 1
            res += arr[i]
            solve(index + 1, res, i + 1)
            res = res[0:int(index)]
            check[i] = 0


solve(0, "", 0)
ans.sort()
for a in range(len(ans)):
    print(ans[a])
