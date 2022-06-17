import sys, collections, heapq
read = sys.stdin.readline

N = int(read())
space = [list(map(int,read().split())) for _ in range(N)]
now = (0,0)
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            now = (i,j)
            break
    if space[now[0]][now[1]] == 9:
        break
space[now[0]][now[1]] = 0
shark_size = 2
eat_cnt = 0
direction = [(-1,0),(0,-1),(0,1),(1,0)]
visited = [[False]*N for _ in range(N)]
visited[now[0]][now[1]] = True

queue = collections.deque([now])
dist = 1
ans = 0
while queue:
    next = []
    for _ in range(len(queue)):
        x, y = queue.popleft()
        for dx, dy in direction:
            if 0 <= x+dx < N and 0 <= y+dy < N and visited[x+dx][y+dy] == False:
                if 0 < space[x+dx][y+dy] < shark_size:
                    heapq.heappush(next,(x+dx,y+dy))
                elif space[x+dx][y+dy] == 0 or space[x+dx][y+dy] == shark_size:
                    queue.append((x+dx,y+dy))
                    visited[x+dx][y+dy] = True
    if next:
        x, y = heapq.heappop(next)
        space[x][y] = 0
        ans += dist
        dist = 1
        eat_cnt += 1
        if eat_cnt >= shark_size*(shark_size+1)//2-1:
            shark_size += 1
        visited = [[False]*N for _ in range(N)]
        queue = collections.deque([(x,y)])
        visited[x][y] = True
    else:
        dist += 1
print(ans)