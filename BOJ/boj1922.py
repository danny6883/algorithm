import sys, heapq
read = sys.stdin.readline
INF = 10**9

N = int(read())
M = int(read())
cost = [[INF]*N for _ in range(N)]
for i in range(N):
  cost[i][i] = 0
for _ in range(M):
  a, b, c = map(int, read().split())
  if a == b:
    continue
  a -= 1
  b -= 1
  cost[a][b] = min(cost[a][b], c)
  cost[b][a] = min(cost[b][a], c)

visited = [False]*N
visited[0] = True
ans = 0

heap = []
for i in range(N):
  heapq.heappush(heap,(cost[0][i],0,i))
for _ in range(N-1):
  while True:
    c, start, end = heapq.heappop(heap)
    if visited[end] == False:
      break
  ans += c
  visited[end] = True
  for i in range(N):
    if visited[i] == False:
      heapq.heappush(heap,(cost[end][i],end,i))
print(ans)
