import sys, collections
read = sys.stdin.readline

n = int(read())
start, end = map(int, read().split())
m = int(read())
neighbors = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, read().split())
    neighbors[x].append(y)
    neighbors[y].append(x)
visited = [False]*(n+1)
queue = collections.deque()
queue.append(start)
visited[start] = True
cnt = 0

while queue and not visited[end]:
    cnt += 1
    for _ in range(len(queue)):
        p = queue.popleft()
        for neighbor in neighbors[p]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
if visited[end]:
    print(cnt)
else:
    print(-1)