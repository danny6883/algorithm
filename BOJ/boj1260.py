import sys, collections
read = sys.stdin.readline

N, M, V = map(int, read().split())
ver = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, read().split())
    ver[x-1].append(y-1)
    ver[y-1].append(x-1)
for v in ver:
    v.sort()
visit = [0 for _ in range(N)]

dfs_ans = []
def dfs(i):
    if visit[i]:
        return
    visit[i] = 1
    dfs_ans.append(i+1)
    for vertex in ver[i]:
        dfs(vertex)
dfs(V-1)
print(*dfs_ans)

visit = [0 for _ in range(N)]
bfs_queue = collections.deque([V-1])
visit[V-1] = 1
bfs_ans = []
while bfs_queue:
    temp = bfs_queue.popleft()
    for vertex in ver[temp]:
        if visit[vertex]:
            continue
        visit[vertex] = 1
        bfs_queue.append(vertex)
    bfs_ans.append(temp+1)
print(*bfs_ans)