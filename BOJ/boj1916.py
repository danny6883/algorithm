import sys, heapq
read = sys.stdin.readline
INF = 2*10**9

N = int(read())
M = int(read())
bus = dict()
for i in range(1,N+1):
    bus[i] = []
for _ in range(M):
    start, end, cost = map(int, read().split())
    bus[start].append((cost,end))
start, end = map(int, read().split())
dist = [INF]*(N+1)
dist[start] = 0
short = [(0,start)]

while short:
    cost, start = heapq.heappop(short)
    if dist[start] < cost:
        continue
    for c, e in bus[start]:
        if dist[e] > dist[start] + c:
            dist[e] = dist[start] + c
            heapq.heappush(short, (dist[e],e))
print(dist[end])