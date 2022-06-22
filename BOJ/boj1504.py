import sys, heapq
read = sys.stdin.readline
INF = 10**9*2

N, E = map(int, read().split())
edges = dict()
for i in range(1,N+1):
    edges[i] = []
for _ in range(E):
    a, b, c = map(int, read().split())
    edges[a].append((c,b))
    edges[b].append((c,a))
v1, v2 = map(int, read().split())

route_v1_v2 = 0
route_v2_v1 = 0
dist = [INF]*(N+1)

def ds(start):
    global dist
    dist = [INF]*(N+1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap,(0,start))
    while heap:
        d, v = heapq.heappop(heap)
        if dist[v] < d:
            continue
        for temp_dist, temp_v in edges[v]:
            if dist[temp_v] > dist[v] + temp_dist:
                dist[temp_v] = dist[v] + temp_dist
                heapq.heappush(heap,(dist[temp_v],temp_v))

ds(1)
route_v1_v2 += dist[v1]
route_v2_v1 += dist[v2]

ds(v1)
route_v1_v2 += dist[v2]
route_v2_v1 += dist[N]

ds(v2)
route_v1_v2 += dist[N]
route_v2_v1 += dist[v1]

ans = min(route_v1_v2, route_v2_v1)
if ans >= INF:
    print(-1)
else:
    print(ans)