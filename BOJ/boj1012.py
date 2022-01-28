import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(read())
ans = []
for _ in range(T):
    M, N, K = map(int, read().split())
    cab = [list(map(int, read().split())) for i in range(K)]
    ground = [[0 for i in range(N)] for j in range(M)]
    for i, j in cab:
        ground[i][j] = 1
    visit = [[0 for i in range(N)] for j in range(M)]
    cnt = 0

    def dfs(x,y):
        if 0 <= x < M and 0 <= y < N and visit[x][y] == 0 and ground[x][y] == 1:
            visit[x][y] += 1
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)

    for i, j in cab:
        if visit[i][j] == 0:
            cnt += 1
            dfs(i,j)
    ans.append(cnt)
print('\n'.join(map(str,ans)))