N = input()
length = len(N) // 2
left = 0
right = 0

for i in range(length):
    left += int(N[i])

for i in range(length, len(N)):
    right += int(N[i])

if left != right:
    print("READY")
else:
    print("LUCKY")
