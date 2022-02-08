import sys
read = sys.stdin.readline

def dfs(x,y,visited,sum_n):
    visited.append((x,y))
    sum_n += paper[x][y]
    if len(visited) == 4:
        if max_n[0] < sum_n:
            max_n[0] = sum_n
    else:
        if x > 0 and (x-1,y) not in visited:
            dfs(x-1,y,visited,sum_n)
        if x < N-1 and (x+1,y) not in visited:
            dfs(x+1,y,visited,sum_n)
        if y > 0 and (x,y-1) not in visited:
            dfs(x,y-1,visited,sum_n)
        if y < M-1 and (x,y+1) not in visited:
            dfs(x,y+1,visited,sum_n)
    visited.pop()

N, M = map(int, read().split())
paper = [list(map(int, read().split())) for i in range(N)]
max_n = [0]
for i in range(N):
    for j in range(M):
        dfs(i,j,[],0)

for i in range(N-1):
    for j in range(M-2):
        sum_n = paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i+1][j+1]
        if max_n[0] < sum_n:
            max_n[0] = sum_n
for i in range(1,N):
    for j in range(M-2):
        sum_n = paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i-1][j+1]
        if max_n[0] < sum_n:
            max_n[0] = sum_n
for i in range(N-2):
    for j in range(M-1):
        sum_n = paper[i][j] + paper[i+1][j] + paper[i+1][j+1] + paper[i+2][j]
        if max_n[0] < sum_n:
            max_n[0] = sum_n
for i in range(N-2):
    for j in range(1,M):
        sum_n = paper[i][j] + paper[i+1][j] + paper[i+1][j-1] + paper[i+2][j]
        if max_n[0] < sum_n:
            max_n[0] = sum_n
print(max_n[0])