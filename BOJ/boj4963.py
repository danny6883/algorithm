import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

move = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def land(x,y,visited):
    if 0 <= x < h and 0 <= y < w and input_map[x][y] == 1 and visited[x][y] == 0:
        visited[x][y] = 1
        for move_x, move_y in move:
            land(x+move_x,y+move_y,visited)

ans = []
while True:
    cnt = 0
    w, h = map(int, read().split())
    if w == 0 and h == 0:
        break
    input_map = [list(map(int, read().rstrip().split())) for _ in range(h)]
    visited = [[0 for i in range(w)] for j in range(h)]
    for i in range(h):
        for j in range(w):
            if input_map[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                land(i,j,visited)
    ans.append(str(cnt))
print('\n'.join(ans))