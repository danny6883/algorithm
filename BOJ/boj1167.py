import sys
read = sys.stdin.readline

V = int(read())
edges = [[] for _ in range(V+1)]
for _ in range(V):
    temp = list(map(int, read().split()))
    i = 1
    while temp[i] != -1:
        edges[temp[0]].append((temp[i],temp[i+1]))
        i += 2

start = 1
stack = [(start,0)]
visited = [False]*(V+1)
longest_way = 0
longest_end = 0
while stack:
    temp_start, temp_way = stack.pop()
    visited[temp_start] = True
    for end, way in edges[temp_start]:
        if visited[end] == False:
            if longest_way < temp_way + way:
                longest_way = temp_way + way
                longest_end = end
            stack.append((end,temp_way + way))

start = longest_end
stack = [(start,0)]
visited = [False]*(V+1)
longest_way = 0
longest_end = 0
while stack:
    temp_start, temp_way = stack.pop()
    visited[temp_start] = True
    for end, way in edges[temp_start]:
        if visited[end] == False:
            if longest_way < temp_way + way:
                longest_way = temp_way + way
                longest_end = end
            stack.append((end,temp_way + way))
print(longest_way)