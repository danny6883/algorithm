import sys
read = sys.stdin.readline

N, M = map(int, read().split())
neighbors = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, read().split())
    a -= 1
    b -= 1
    neighbors[a].append(b)
    neighbors[b].append(a)
for i in range(N):
    queue = [i]
    visited = [0 for _ in range(N)]
    visited[i] = 1
    cnts = [0 for _ in range(N)]
    cnt = 0
    while queue:
        for j in range(len(queue)):
            k = queue.pop(0)
            cnts[k] = cnt
            for neighbor in neighbors[k]:
                if visited[neighbor] == 0:
                    visited[neighbor] += 1
                    queue.append(neighbor)
        cnt += 1
    if i == 0 or min_cnt[1] > sum(cnts):
        min_cnt = [i+1, sum(cnts)]
print(min_cnt[0])