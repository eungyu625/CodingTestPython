import sys

input = sys.stdin.readline

r, c, k = map(int, input().split())
arr = []

for _ in range(r):
    arr.append(list(map(int, input().split())))

