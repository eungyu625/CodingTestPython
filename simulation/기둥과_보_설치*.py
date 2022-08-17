def check(result):
    for x, y, stuff in result:
        if stuff == 0:
            if y == 0 or [x - 1, y, 1] in result or [x, y, 1] in result or [x, y - 1, 0] in result:
                continue
            return False
        else:
            if [x, y - 1, 0] in result or [x + 1, y - 1, 0] in result or\
                    ([x - 1, y, 1] in result and [x + 1, y, 1] in result):
                continue
            return False
    return True


def solution(n, build_frame):
    result = []
    for x, y, stuff, operate in build_frame:
        if operate == 0:
            result.remove([x, y, stuff])
            if not check(result):
                result.append([x, y, stuff])
        else:
            result.append([x, y, stuff])
            if not check(result):
                result.remove([x, y, stuff])

    return result
