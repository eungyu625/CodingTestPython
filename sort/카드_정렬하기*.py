import heapq

N = int(input())
heap = []

for _ in range(N):
    heapq.heappush(heap, int(input()))

answer = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    answer += one + two
    heapq.heappush(heap, one + two)

print(answer)
