import sys, heapq
read = sys.stdin.readline

ans = []
heap = []
for _ in range(int(read())):
    x = int(read())
    if x:
        heapq.heappush(heap,(abs(x),x))
    else:
        if heap:
            ans.append(heapq.heappop(heap)[1])
        else:
            ans.append(0)
print('\n'.join(map(str,ans)))