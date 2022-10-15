import sys, heapq
read = sys.stdin.readline

N = int(read())
s_heap = []
t_heap = []
for _ in range(N):
    s, t = map(int, read().split())
    heapq.heappush(s_heap,s)
    heapq.heappush(t_heap,t)

ans = 1
now = 0
while s_heap:
    if s_heap[0] < t_heap[0]:
        heapq.heappop(s_heap)
        now += 1
        ans = max(ans,now)
    elif s_heap[0] == t_heap[0]:
        heapq.heappop(s_heap)
        heapq.heappop(t_heap)
    else:
        heapq.heappop(t_heap)
        now -= 1
print(ans)