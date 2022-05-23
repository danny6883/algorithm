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










# import sys, heapq
# read = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# def ds(i):
#     for end, dist in edges[i]:
#         if visited[end] == False:
#             if len_v[i]+dist > len_v[end]:
#                 len_v[end] = len_v[i]+dist
#                 heapq.heappush(heap,(-dist,end))
#     visited[i] = True
#     next = heapq.heappop(heap)[1]
#     while heap and visited[next] == True:
#         next = heapq.heappop(heap)[1]
#     print('----------')
#     print(i)
#     print(len_v)
#     if heap == []:
#         return
#     ds(next)

# V = int(read())
# ans = 0
# len_v = [0]*(V+1)
# visited = [False]*(V+1)
# edges = [[] for _ in range(V+1)]
# heap = [(0,i) for i in range(1,V+1)]
# for _ in range(V):
#     temp = list(map(int, read().split()))
#     i = 1
#     while temp[i] != -1:
#         edges[temp[0]].append((temp[i],temp[i+1]))
#         i += 2
# ds(4)
# visited[4] = False
# ds(5)
# print(max(len_v))