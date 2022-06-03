import sys
read = sys.stdin.readline

MAX = 9876543210
TC = int(read())
for _ in range(TC):
    N, M, W = map(int, read().split())
    dist = [MAX]*(N+1)
    dist[1] = 0
    edges = []
    for i in range(M):
        S, E, T = map(int, read().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    for i in range(W):
        S, E, T = map(int, read().split())
        edges.append((S, E, -T))
    ans = "NO"
    for i in range(N-1):
        for edge in edges:
            now = edge[0]
            next = edge[1]
            time = edge[2]
            if dist[next] > dist[now] + time:
                dist[next] = dist[now] + time
    for edge in edges:
        now = edge[0]
        next = edge[1]
        time = edge[2]
        if dist[next] > dist[now] + time:
            ans = "YES"
            break
    print(ans)