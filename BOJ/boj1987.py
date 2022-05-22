import sys
read = sys.stdin.readline
R, C = map(int, read().split())
board = [read().rstrip() for _ in range(R)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y,visited,m):
    ans = m
    temp_visited = visited[:]
    temp_visited[ord(board[x][y])-ord('A')] = True
    for i in range(4):
        if 0<=x+dx[i]<R and 0<=y+dy[i]<C and temp_visited[ord(board[x+dx[i]][y+dy[i]])-ord('A')] == False:
            ans = max(ans, dfs(x+dx[i],y+dy[i],temp_visited,m+1))
    return ans
print(dfs(0,0,[False]*26,1))