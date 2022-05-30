import sys, collections
read = sys.stdin.readline

R, C = map(int, read().split())
block = [list(map(int, read().split())) for _ in range(R)]
N = int(read())
rules = [list(map(int, read().split())) for _ in range(N)]

visited = [[False]*C for _ in range(R)]
queue = collections.deque()
for i in range(C):
    if block[0][i] == 1:
        queue.append((0,i))
        visited[0][i] = True
ans = 0
can_go = False
if R == 1 and queue:
    can_go = True
while queue and can_go == False:
    for _ in range(len(queue)):
        if can_go:
            break
        now_R, now_C = queue.popleft()
        for dx, dy in rules:
            temp_R = now_R + dx
            temp_C = now_C + dy
            if 0 <= temp_R < R and 0 <= temp_C < C and block[temp_R][temp_C] == 1 and visited[temp_R][temp_C] == False:
                if temp_R == R-1:
                    can_go = True
                    break
                queue.append((temp_R,temp_C))
                visited[temp_R][temp_C] = True
    ans += 1
if can_go:
    print(ans)
else:
    print(-1)