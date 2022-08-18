N = int(input())
arr = list(map(int, input().split()))


def solution(start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if mid == arr[mid]:
        return mid
    elif mid > arr[mid]:
        return solution(mid + 1, end)
    else:
        return solution(start, mid - 1)


print(solution(0, N))
