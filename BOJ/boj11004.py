import heapq

N, K = map(int, input().split())
A_nums = list(map(int, input().split()))
heap = [-A_nums[i] for i in range(K)]
heapq.heapify(heap)
for i in range(K,N):
    if -heap[0] > A_nums[i]:
        heapq.heappop(heap)
        heapq.heappush(heap,-A_nums[i])
print(-heap[0])