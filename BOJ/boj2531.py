import sys, collections
read = sys.stdin.readline

N, d, k, c = map(int, read().split())
belt = [int(read()) for _ in range(N)]

queue = collections.deque(belt[:k])
kind = set(queue)
len_kind = len(kind)
ans = 0
if c in kind:
    ans = max(ans, len_kind)
else:
    ans = max(ans, len_kind + 1)
    
for i in range(k,N+k):
    left = queue.popleft()
    right = belt[i%N]

    if left not in queue:
        kind.remove(left)
        len_kind -= 1
    queue.append(right)
    if right not in kind:
        kind.add(right)
        len_kind += 1

    if c in kind:
        ans = max(ans, len_kind)
    else:
        ans = max(ans, len_kind + 1)
print(ans)