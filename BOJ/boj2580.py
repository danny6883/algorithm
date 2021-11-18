import sys
board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zeros = [(x,y) for x in range(9) for y in range(9) if board[x][y] == 0]
def case(x, y):
    nums = [i+1 for i in range(9)]
    for i in range(9):
        if board[i][y] in nums:
            nums.remove(board[i][y])
        if board[x][i] in nums:
            nums.remove(board[x][i])
    temp_x = (x // 3) * 3
    temp_y = (y // 3) * 3
    for i in range(temp_x, temp_x+3):
        for j in range(temp_y, temp_y+3):
            if board[i][j] in nums:
                nums.remove(board[i][j])
    return nums

def dfs(change):
    if len(zeros) == change:
        for row in board:
            print(' '.join(map(str, row)))
        sys.exit()
    i, j = zeros[change][:]
    nums = case(i, j)
    for num in nums:
        board[i][j] = num
        dfs(change + 1)
        board[i][j] = 0

dfs(0)