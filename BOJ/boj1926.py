import sys, collections
read = sys.stdin.readline

n, m = map(int, read().split())
picture = [list(map(int, read().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
direction = [(0,-1),(0,1),(-1,0),(1,0)]
queue = collections.deque()
cnt = 0
max_size = 0
for i in range(n):
    for j in range(m):
        if picture[i][j] == 1 and visited[i][j] == False:
            queue = collections.deque([(i,j)])
            cnt += 1
            size = 1
            visited[i][j] = True
            while queue:
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    for dx, dy in direction:
                        if 0 <= x+dx < n and 0 <= y+dy < m and picture[x+dx][y+dy] == 1 and visited[x+dx][y+dy] == False:
                            queue.append((x+dx,y+dy))
                            visited[x+dx][y+dy] = True
                            size += 1
            max_size = max(max_size, size)
print(cnt)
print(max_size)