import sys, collections
read = sys.stdin.readline

N, M = map(int, read().split())
child = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, read().split())
    child[B].append(A)

child_cnt = [0]*(N+1)
for i in range(1,N+1):
    visited = [False]*(N+1)
    queue = collections.deque([i])
    visited[i] = True
    while queue:
        for _ in range(len(queue)):
            temp = queue.popleft()
            for c in child[temp]:
                if not visited[c]:
                    queue.append(c)
                    visited[c] = True
                    child_cnt[i] += 1

ans = []
max_child = -1
for i in range(1,N+1):
    if child_cnt[i] > max_child:
        max_child = child_cnt[i]
        ans = [i]
    elif child_cnt[i] == max_child:
        ans.append(i)
print(*ans)