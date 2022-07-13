import sys
read = sys.stdin.readline

N = int(read())
home = [list(map(int, read().split()))+[0] for _ in range(N)]
home.append([0]*(N+1))
board = [[[0,0,0] for i in range(N+1)] for j in range(N+1)]
board[0][1][0] = 1
for i in range(1,N):
    for j in range(i):
        if not home[i][j+1]:
            board[i][j+1][0] += board[i][j][0]
            board[i][j+1][0] += board[i][j][1]
            if not home[i+1][j] and not home[i+1][j+1]:
                board[i+1][j+1][1] += sum(board[i][j])
        if not home[i+1][j]:
                board[i+1][j][2] += board[i][j][1]
                board[i+1][j][2] += board[i][j][2]
    for j in range(i):
        if not home[j+1][i]:
            board[j+1][i][2] += board[j][i][1]
            board[j+1][i][2] += board[j][i][2]
            if not home[j][i+1] and not home[j+1][i+1]:
                board[j+1][i+1][1] += sum(board[j][i])
        if not home[j][i+1]:
                board[j][i+1][0] += board[j][i][1]
                board[j][i+1][0] += board[j][i][0]
    if not home[i+1][i]:
        board[i+1][i][2] += board[i][i][1]
        board[i+1][i][2] += board[i][i][2]
        if not home[i][i+1] and not home[i+1][i+1]:
            board[i+1][i+1][1] += sum(board[i][i])
    if not home[i][i+1]:
            board[i][i+1][0] += board[i][i][1]
            board[i][i+1][0] += board[i][i][0]
print(sum(board[N-1][N-1]))