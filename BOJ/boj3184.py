import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

R, C = map(int, read().split())
board = [read().rstrip() for _ in range(R)]
visited = [[False]*C for _ in range(R)]
dir = ((0,-1),(0,1),(-1,0),(1,0))
temp_sheep_wolf = [0,0]
ans = [0,0]

def same_area(i,j):
    visited[i][j] = True
    if board[i][j] == 'o':
        temp_sheep_wolf[0] += 1
    elif board[i][j] == 'v':
        temp_sheep_wolf[1] += 1
    for dx,dy in dir:
        if 0 <= i+dx < R and 0 <= j+dy < C and board[i+dx][j+dy] != '#' and visited[i+dx][j+dy] == False:
            same_area(i+dx,j+dy)
        
for i in range(R):
    for j in range(C):
        if board[i][j] != '#' and visited[i][j] == False:
            same_area(i,j)
            if temp_sheep_wolf[0] > temp_sheep_wolf[1]:
                ans[0] += temp_sheep_wolf[0]
            else:
                ans[1] += temp_sheep_wolf[1]
            temp_sheep_wolf = [0,0]
print(*ans)