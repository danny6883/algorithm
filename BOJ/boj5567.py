import sys
read = sys.stdin.readline

n = int(read())
m = int(read())
neighbors = dict()
for i in range(1,n+1):
    neighbors[i] = []
for _ in range(m):
    a, b = map(int, read().split())
    neighbors[a].append(b)
    neighbors[b].append(a)
visited = [False]*(n+1)
visited[1] = True
ans = 0
for n in neighbors[1]:
    visited[n] = True
    ans += 1
for n in neighbors[1]:
    for n2 in neighbors[n]:
        if visited[n2] == False:
            visited[n2] = True
            ans += 1
print(ans)