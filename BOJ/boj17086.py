import collections, sys
read = sys.stdin.readline

N, M = map(int, read().split())
space = [list(map(int, read().split())) for _ in range(N)]
safe_length = [[100]*M for _ in range(N)]
directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

for i in range(N):
    for j in range(M):
        if space[i][j] == 1:
            safe_length[i][j] = 0

for i in range(N):
    for j in range(M):
        if space[i][j] == 1:
            visited = [[False]*M for _ in range(N)]
            queue = collections.deque()
            queue.append((i,j))
            visited[i][j] = True

            changed = True
            cnt = 0
            while changed:
                changed = False
                cnt += 1
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    for dx, dy in directions:
                        mx = x + dx
                        my = y + dy
                        if 0 <= mx < N and 0 <= my < M and not visited[mx][my]:
                            if safe_length[mx][my] > cnt:
                                changed = True
                                safe_length[mx][my] = cnt
                            queue.append((mx,my))
                            visited[mx][my] = True

ans = max([max(row) for row in safe_length])
print(ans)