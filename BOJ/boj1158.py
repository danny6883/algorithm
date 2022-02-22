import collections
N, K = map(int, input().split())
queue = collections.deque(range(1,N+1))
yosepus = []
while queue:
    queue.rotate(-K+1)
    yosepus.append(queue.popleft())
print('<' + ', '.join(map(str,yosepus)) + '>')