import sys, collections
read = sys.stdin.readline

N, M, K, X = map(int, read().split())
roads = dict()
for i in range(N+1):
    roads[i] = []
for _ in range(M):
    start, end = map(int, read().split())
    roads[start].append(end)
queue = collections.deque()
queue.append(X)
visited = [False]*(N+1)
visited[X] = True
ans = []
len_road = 0
while queue:
    for _ in range(len(queue)):
        temp = queue.popleft()
        for neighbor in roads[temp]:
            if visited[neighbor] == False:
                visited[neighbor] = True
                queue.append(neighbor)
    len_road += 1
    if len_road == K:
        ans = list(queue)[:]
        break
if ans == []:
    print(-1)
else:
    ans.sort()
    print('\n'.join(map(str,ans)))