
n = int(input())
m = int(input())

button = []

if m != 0:
    button = list(map(int, input().split()))

ans = abs(n - 100)

cipher = 0
count_cipher = n
while count_cipher:
    count_cipher //= 10
    cipher += 1

if n == 0:
    cipher = 1


def answer(res, result):
    result += abs(n - res)
    global ans
    if ans > result:
        ans = result
    return


def solve(index, res, result):
    if index == cipher + 1:
        return

    for i in range(10):
        if i not in button:
            num = i
            for _ in range(index):
                num *= 10
            answer(res + num, result + 1)
            solve(index + 1, res + num, result + 1)


solve(0, 0, 0)
print(ans)
