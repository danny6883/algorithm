import sys, heapq
read = sys.stdin.readline

n = int(read())
heap = []
ans = []
for _ in range(n):
    x = int(read())
    if x:
        heapq.heappush(heap,-x)
    else:
        if heap:
            ans.append(-heapq.heappop(heap))
        else:
            ans.append(0)
print('\n'.join(map(str,ans)))