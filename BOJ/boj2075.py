import sys,heapq
read = sys.stdin.readline
n = int(read())
stacks = [[] for _ in range(n)]
 
heap = list(map(int, read().split()))
heapq.heapify(heap)
for _ in range(n-1):
  row = list(map(int, read().split()))
  for i in range(n):
    heapq.heappush(heap, row[i])
    heapq.heappop(heap)
print(heapq.heappop(heap))