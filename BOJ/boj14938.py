import sys
read = sys.stdin.readline
INF = 10**9

n, m, r = map(int, read().split())
items = list(map(int, read().split()))
roads = [[INF]*n for _ in range(n)]
for i in range(n):
    roads[i][i] = 0
neighbors = [[] for _ in range(n)]
for _ in range(r):
    a, b, l = map(int, read().split())
    a -= 1
    b -= 1
    roads[a][b] = min(roads[a][b],l)
    roads[b][a] = roads[a][b]
for k in range(n):
    for i in range(n):
        for j in range(n):
            roads[i][j] = min(roads[i][j], roads[i][k]+roads[k][j])

ans = 0
for i in range(n):
    temp = 0
    for j in range(n):
        if roads[i][j] <= m:
            temp += items[j]
    ans = max(ans, temp)
print(ans)