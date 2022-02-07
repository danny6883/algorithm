import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,y,visited):
    visited[x][y] += 1
    if y > 0 and visited[x][y-1] == 0 and picture[x][y] == picture[x][y-1]:
        dfs(x,y-1,visited)
    if y < N-1 and visited[x][y+1] == 0 and picture[x][y] == picture[x][y+1]:
        dfs(x,y+1,visited)
    if x > 0 and visited[x-1][y] == 0 and picture[x][y] == picture[x-1][y]:
        dfs(x-1,y,visited)
    if x < N-1 and visited[x+1][y] == 0 and picture[x][y] == picture[x+1][y]:
        dfs(x+1,y,visited)

def dfs_rg_or_b(x,y,visited,rg_or_b):
    visited[x][y] += 1
    if y > 0 and visited[x][y-1] == 0 and picture[x][y-1] in rg_or_b:
        dfs_rg_or_b(x,y-1,visited,rg_or_b)
    if y < N-1 and visited[x][y+1] == 0 and picture[x][y+1] in rg_or_b:
        dfs_rg_or_b(x,y+1,visited,rg_or_b)
    if x > 0 and visited[x-1][y] == 0 and picture[x-1][y] in rg_or_b:
        dfs_rg_or_b(x-1,y,visited,rg_or_b)
    if x < N-1 and visited[x+1][y] == 0 and picture[x+1][y] in rg_or_b:
        dfs_rg_or_b(x+1,y,visited,rg_or_b)

N = int(read())
picture = [read().rstrip() for i in range(N)]
visited = [[0 for i in range(N)] for j in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i,j,visited)
            cnt += 1

cnt2 = 0
visited = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            if picture[i][j] == 'B':
                dfs_rg_or_b(i,j,visited,'B')
            else:
                dfs_rg_or_b(i,j,visited,'RG')
            cnt2 += 1
print(cnt, cnt2)