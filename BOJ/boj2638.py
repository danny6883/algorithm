import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, read().split())
board = [list(map(int, read().split())) for _ in range(N)]

def check_air(i,j):
    if board[i][j]:
        cnt = 0
        if air[i][j-1]:
            cnt += 1
        if air[i][j+1]:
            cnt += 1
        if air[i-1][j]:
            cnt += 1
        if air[i+1][j]:
            cnt += 1
        if cnt >= 2:
            board[i][j] = 0
            return True
        else:
            return False
    else:
        return False

def spread_air(i,j):
    air[i][j] = True
    for dx, dy in ((0,-1),(0,1),(-1,0),(1,0)):
        if 0 <= i+dx < N and 0 <= j+dy < M and air[i+dx][j+dy] == False and board[i+dx][j+dy] == 0:
            spread_air(i+dx,j+dy)

air = [[False]*M for _ in range(N)]
spread_air(0,0)

ans = 0
while True:
    melt = []
    for i in range(N):
        for j in range(M):
            if check_air(i,j):
                melt.append((i,j))
    if melt == []:
        break
    for i, j in melt:
        spread_air(i,j)
    ans += 1
print(ans)