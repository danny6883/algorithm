import sys, collections
read = sys.stdin.readline

N, M = map(int, read().split())
input_map = [read().rstrip() for _ in range(N)]
visit = [[[0,0] for i in range(M)] for j in range(N)]
visit[0][0][0] = 1
visit[0][0][1] = 1
queue = collections.deque([(0,0,0)])
cnt = 1

def neighbor(x,y,wall):
    if 0 <= x < N and 0 <= y < M:
        if visit[x][y][wall] == 0 and input_map[x][y] == '0':
            visit[x][y][wall] += 1
            queue.append((x,y,wall))
        elif wall == 0 and visit[x][y][1] == 0 and input_map[x][y] == '1':
            visit[x][y][1] += 1
            queue.append((x,y,1))

while queue:
    if visit[N-1][M-1][0] or visit[N-1][M-1][1]:
        break
    for _ in range(len(queue)):
        x,y,wall = queue.popleft()
        neighbor(x+1,y,wall)
        neighbor(x-1,y,wall)
        neighbor(x,y-1,wall)
        neighbor(x,y+1,wall)
    cnt += 1
if visit[N-1][M-1][0] or visit[N-1][M-1][1]:
    print(cnt)
else:
    print('-1')