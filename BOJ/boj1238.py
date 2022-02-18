import sys, heapq
read = sys.stdin.readline

N, M, X = map(int, read().split())
roads = [[] for i in range(N+1)]
roads_reverse = [[] for i in range(N+1)]
for i in range(M):
    start, end, time = map(int, read().split())
    roads[start].append((end,time))
    roads_reverse[end].append((start,time))
x_to_i_time = [987654321]*(N+1)
i_to_x_time = [987654321]*(N+1)

heap = [(0,X)]
while heap:
    time, town = heapq.heappop(heap)
    for r_end, r_time in roads[town]:
        if x_to_i_time[r_end] > r_time+time:
            x_to_i_time[r_end] = r_time+time
            heapq.heappush(heap,(r_time+time,r_end))

heap = [(0,X)]
while heap:
    time, town = heapq.heappop(heap)
    for r_start, r_time in roads_reverse[town]:
        if i_to_x_time[r_start] > r_time+time:
            i_to_x_time[r_start] = r_time+time
            heapq.heappush(heap,(r_time+time,r_start))

max_time = 0
x_to_i_time[X] = 0
i_to_x_time[X] = 0
for i in range(1,N+1):
    if max_time < x_to_i_time[i] + i_to_x_time[i]:
        max_time = x_to_i_time[i] + i_to_x_time[i]
print(max_time)