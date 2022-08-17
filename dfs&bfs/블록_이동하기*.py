def get_next_pos(pos, new_board):
    next_pos = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(4):
        pos1_next_x, pos1_next_y = pos1_x + dx[i], pos1_y + dy[i]
        pos2_next_x, pos2_next_y = pos2_x + dx[i], pos2_y + dy[i]
        if new_board[pos1_next_x][pos1_next_y] == 0 and new_board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
    if pos1_x == pos2_x:
        for i in [-1, 1]:
            if new_board[pos1_x + i][pos1_y] == 0 and new_board[pos2_x + i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    elif pos1_y == pos2_y:
        for i in [-1,1]:
            if new_board[pos1_x][pos1_y + i] == 0 and new_board[pos2_x][pos2_y + i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})

    return next_pos


def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    queue = [({(1, 1), (1, 2)}, 0)]
    visited = [{(1, 1,), (1, 2)}]

    while queue:
        pos, cost = queue.pop(0)
        if (n, n) in pos:
            return cost

        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                queue.append((next_pos, cost + 1))
                visited.append(next_pos)

    return 0
