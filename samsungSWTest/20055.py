N, K = map(int, input().split())
belt = list(map(int, input().split()))  # 올리는 위치 : 0, 내리는 위치 : N - 1
robot = [0] * N
ans = 0

while True:
    ans += 1
    belt_temp = belt[0]
    robot_temp = robot[0]
    for i in range(1, len(belt)):
        belt[i], belt_temp = belt_temp, belt[i]
    belt[0] = belt_temp
    for i in range(1, len(robot)):
        robot[i], robot_temp = robot_temp, robot[i]
    robot[0] = 0
    robot[N - 1] = 0
    for i in range(len(robot) - 1, 0, -1):
        if robot[i] == 1:
            if robot[i + 1] == 0 and belt[i + 1] != 0:
                robot[i + 1] = 1
                robot[i] = 0
                belt[i + 1] -= 1
    robot[N - 1] = 0
    robot[N - 1] = 0
    if belt[0] != 0:
        robot[0] = 1
        belt[0] -= 1
    res = 0
    for i in range(len(belt)):
        if belt[i] == 0:
            res += 1
    if res >= K:
        break

print(ans)
