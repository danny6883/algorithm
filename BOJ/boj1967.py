n = int(input())
edges = [list(map(int, input().split())) for _ in range(n-1)]
edges.sort(key=lambda k: k[1], reverse=True)
ans = 0
nodes = [0]*(n+1)
for i in range(n-1):
    if ans < nodes[edges[i][0]] + nodes[edges[i][1]] + edges[i][2]:
        ans = nodes[edges[i][0]] + nodes[edges[i][1]] + edges[i][2]
    if nodes[edges[i][0]] < nodes[edges[i][1]] + edges[i][2]:
        nodes[edges[i][0]] = nodes[edges[i][1]] + edges[i][2]
print(ans)