import sys,collections,heapq
read = sys.stdin.readline

V, E = map(int, read().split())
K = int(read())
neighbors = [[] for i in range(V+1)]
for i in range(E):
    u, v, w = map(int, read().split())
    neighbors[u].append((v,w))

route = [987654321]*(V+1)
route[K] = 0
hq = []
heapq.heappush(hq, (0,K))
while hq:
    route_w, route_v = heapq.heappop(hq)
    for v, w in neighbors[route_v]:
        if route[v] > w+route_w:
            route[v] = w+route_w
            heapq.heappush(hq, (w+route_w,v))

for i in range(1,V+1):
    if route[i] == 987654321:
        print('INF')
    else:
        print(route[i])