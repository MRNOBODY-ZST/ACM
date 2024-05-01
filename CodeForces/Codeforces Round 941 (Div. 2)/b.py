t = int(input())


def col_check(pattern_num: int, color: str):
    if pattern_num == 0:
        col = -1
    else:
        col = 0
    for i in range(0, n):
        if grid[i][col] == color:
            return True
    return False


def row_check(pattern_num: int, color: str):
    if pattern_num == 1:
        row = 0
    else:
        row = -1
    for i in range(0, m):
        if grid[row][i] == color:
            return True
    return False


for _ in range(t):
    n, m = map(int, input().split())
    grid = []
    flag = 0
    pattern_list = [
        [[0, 0], [-1, 0]],
        [[-1, -0], [-1, -1]],
        [[-1, -1], [0, -1]],
        [[0, -1], [0, 0]],
    ]
    pattern_against = []
    for i in range(n):
        grid.append(input())
    if grid[0][0] == grid[-1][-1]:
        flag += 1
    if grid[0][-1] == grid[-1][0]:
        flag += 1
    for j in range(4):
        pattern = pattern_list[j]
        if grid[pattern[0][0]][pattern[0][1]] == grid[pattern[1][0]][pattern[1][1]]:
            pattern_against.append([j, grid[pattern[0][0]][pattern[0][1]]])
    for item in pattern_against:
        if item[0] % 2 == 0:
            if col_check(item[0], item[1]):
                flag += 1
        else:
            if row_check(item[0], item[1]):
                flag += 1
    if flag > 0:
        print("Yes")
    else:
        print("No")
