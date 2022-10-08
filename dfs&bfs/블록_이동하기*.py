def get_next_pos(pos, new_board):
    get_pos = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        pos1_next_x, pos1_next_y = pos1_x + dx[i], pos1_y + dy[i]
        pos2_next_x, pos2_next_y = pos2_x + dx[i], pos2_y + dy[i]
        if new_board[pos1_next_x][pos1_next_y] == 0 and new_board[pos2_next_x][pos2_next_y] == 0:
            get_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
    if pos1_x == pos2_x:
        for i in [-1, 1]:
            if new_board[pos1_x + i][pos1_y] == 0 and new_board[pos2_x + i][pos2_y] == 0:
                get_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                get_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    elif pos1_y == pos2_y:
        for i in [-1, 1]:
            if new_board[pos1_x][pos1_y + i] == 0 and new_board[pos2_x][pos2_y + i] == 0:
                get_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                get_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})

    return get_pos


def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]

    for i in range(n):
        for j in range(n):
            new_board[i][j] = board[i][j]

    q = [({(1, 1), (1, 2)}, 0)]
    visited = []

    while q:
        pos, cost = q.pop(0)
        if (n, n) in pos:
            return cost
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)

    return 0

