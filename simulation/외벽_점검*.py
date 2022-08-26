from itertools import permutations


def solution(n, weak, dist):
    result = len(dist) + 1
    length = len(weak)

    for i in range(length):
        weak.append(weak[i] + n)

    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count - 1]
            for index in range(start + length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
            result = min(result, count)

    if result > len(dist):
        return -1

    return result
