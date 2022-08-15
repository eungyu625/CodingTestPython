
def check(string):
    count = 0
    for st in string:
        if st == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return True


def solution(p):
    if p == "":
        return ""
    result = ""
    count = 0
    u = ""
    v = ""

    for step in range(len(p)):
        s = p[step]
        if s == "(":
            u += s
            count += 1
        else:
            u += s
            count -= 1
        if count == 0:
            v = p[step + 1:len(p)]
            break

    if check(u):
        result += u + solution(v)
    else:
        result += "(" + solution(v) + ")"
        for i in range(1, len(u) - 1):
            if u[i] == "(":
                result += ")"
            else:
                result += "("
    return result


print(solution(input()))
