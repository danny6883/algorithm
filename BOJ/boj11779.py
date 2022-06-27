import sys, heapq
read = sys.stdin.readline
INF = 2*10**9

n = int(read())
m = int(read())
bus = dict()
for i in range(1,n+1):
    bus[i] = []
for _ in range(m):
    start, end, cost = map(int, read().split())
    bus[start].append((cost,end))
start, end = map(int, read().split())
dist = [INF]*(n+1)
dist[start] = 0
short = [(0,start)]
path = [[] for _ in range(n+1)]
while short:
    cost, start = heapq.heappop(short)
    if dist[start] < cost:
        continue
    for temp_cost, temp_end in bus[start]:
        if dist[temp_end] > dist[start] + temp_cost:
            dist[temp_end] = dist[start] + temp_cost
            heapq.heappush(short, (dist[temp_end],temp_end))
            path[temp_end] = path[start] + [start]
path[end].append(end)
print(dist[end])
print(len(path[end]))
print(*path[end])