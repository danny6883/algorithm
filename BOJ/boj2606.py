import sys
read = sys.stdin.readline

com_n = int(read())
edge_n = int(read())
edges = [list(map(int, read().split())) for _ in range(edge_n)]
neighbors = [[] for _ in range(com_n+1)]
for edge in edges:
    neighbors[edge[0]].append(edge[1])
    neighbors[edge[1]].append(edge[0])
visit = [0 for _ in range(com_n+1)]
visit[1] = 1
queue = [1]
count = -1
while queue:
    virus = queue.pop(0)
    count += 1
    for neighbor in neighbors[virus]:
        if visit[neighbor] == 0:
            queue.append(neighbor)
            visit[neighbor] = 1
print(count)