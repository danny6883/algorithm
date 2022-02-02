import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(n):
    for vertex in neighbors[n]:
        if visited[vertex] == 0:
            visited[vertex] += 1
            dfs(vertex)

N, M = map(int, read().split())
neighbors = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, read().split())
    u -= 1
    v -= 1
    neighbors[u].append(v)
    neighbors[v].append(u)
visited = [0 for _ in range(N)]
cnt = 0
for i in range(N):
    if visited[i] == 0:
        cnt += 1
        dfs(i)
print(cnt)