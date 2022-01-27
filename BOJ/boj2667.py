import sys
read = sys.stdin.readline

N = int(read())
input_map = [read().rstrip() for _ in range(N)]
visit = [[0 for i in range(N)] for j in range(N)]
ans = []

def dfs(x,y):
    if 0 <= x < N and 0 <= y < N and input_map[x][y] == '1' and visit[x][y] == 0:
        stack.append((x,y))
        visit[x][y] += 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)

for i in range(N):
    for j in range(N):
        if input_map[i][j] == '1' and visit[i][j] == 0:
            stack = []
            dfs(i,j)
            ans.append(len(stack))
ans.sort()
print(len(ans))
print('\n'.join(map(str,ans)))