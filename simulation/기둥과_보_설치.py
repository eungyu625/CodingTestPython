def check(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            if y == 0 or [x, y - 1, 1] in answer or [x - 1, y - 1, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        else:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer \
                    or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False


def solution(n, build_frame):
    answer = []

    for x, y, a, b in build_frame:
        if b == 0:
            answer.remove([x, y, a])
            if not check(answer):
                answer.append([x, y, a])
        else:
            answer.append([x, y, a])
            if not check(answer):
                answer.remove([x, y, a])

    return answer
