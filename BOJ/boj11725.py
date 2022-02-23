import sys, collections
read = sys.stdin.readline

N = int(read())
neighbors = [[] for _ in range(N+1)]
for _ in range(N-1):
    v1, v2 = map(int, read().split())
    neighbors[v1].append(v2)
    neighbors[v2].append(v1)
parents = [0]*(N-1)
visited = [1,1]+[0]*(N-1)
queue = collections.deque([1])
while queue:
    for _ in range(len(queue)):
        parent = queue.popleft()
        for child in neighbors[parent]:
            if visited[child] == 0:
                visited[child] += 1
                parents[child-2] = parent
                queue.append(child)
print('\n'.join(map(str,parents)))