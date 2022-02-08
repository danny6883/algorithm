import sys, collections
read = sys.stdin.readline

N = int(read())
graph = [list(map(int, read().split())) for i in range(N)]
i_to_j = []
for i in range(N):
    temp = []
    for j in range(N):
        if graph[i][j] == 1:
            temp.append(j)
    i_to_j.append(temp)

ans = []
len_ans = 0
for start_i in range(N):
    visited = [0]*N
    queue = collections.deque([start_i])
    while queue:
        for i in range(len(queue)):
            start = queue.popleft()
            if start < len_ans:
                for j in range(N):
                    if ans[start][j] == 1:
                        visited[j] = 1
                continue
            for end in i_to_j[start]:
                if visited[end] == 0:
                    visited[end] = 1
                    queue.append(end)
    ans.append(visited)
    len_ans += 1
for row in ans:
    print(*row)