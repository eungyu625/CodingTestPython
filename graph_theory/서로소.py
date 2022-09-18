v, e = map(int, input().split())
parent = [0] * (v + 1)


def find_parent(num):
    if parent[num] != num:
        parent[num] = find_parent(parent[num])
    return parent[num]


def union_parent(num1, num2):
    child_a = find_parent(num1)
    child_b = find_parent(num2)
    if child_a < child_b:
        parent[child_b] = child_a
    else:
        parent[child_a] = child_b


for i in range(1, v + 1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(a, b)

print("각 원소가 속한 집합 : ", end='')
for i in range(1, v + 1):
    print(find_parent(i), end=' ')

print()

print("부모 테이블 : ", end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')
