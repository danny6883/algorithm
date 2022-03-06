import sys
read = sys.stdin.readline

N, M = map(int, read().split())
board = [list(map(int,read().split())) for _ in range(N)]
for i in range(N):
    for j in range(1,len(board[i])):
        board[i][j] += board[i][j-1]
for i in range(1,N):
    for j in range(len(board[i])):
        board[i][j] += board[i-1][j]

ans = []
for _ in range(M):
    x1, y1, x2, y2 = map(int, read().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    if 1 <= x1 and 1 <= y1:
        temp = board[x2][y2] - board[x1-1][y2] - board[x2][y1-1] + board[x1-1][y1-1]
    elif x1 == 0:
        if y1 == 0:
            temp = board[x2][y2]
        else: # 1 <= y1
            temp = board[x2][y2] - board[x2][y1-1]
    else: # 1 <= x1 and y1 == 0
        temp = board[x2][y2] - board[x1-1][y2]
    ans.append(str(temp))
print('\n'.join(ans))