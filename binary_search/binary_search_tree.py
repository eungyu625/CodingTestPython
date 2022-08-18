
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] > target:
        binary_search(array, target, start, mid - 1)
    elif array[mid] < target:
        binary_search(array, target, mid + 1, start)
    else:
        return mid
    