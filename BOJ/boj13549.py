import collections
N, K = map(int, input().split())
time = 0
cases = collections.deque()
visited = [False] * 100001

def append_case(now):
    while now%2 == 0:
        if visited[now]:
            break
        visited[now] = True
        cases.append(now)
        now //= 2
    if visited[now] == False:
        visited[now] = True
        cases.append(now)

temp_K = K
if temp_K:
    while temp_K%2 == 0:
            visited[temp_K] = True
            cases.append(temp_K)
            temp_K //= 2
visited[temp_K] = True
cases.append(temp_K)

while visited[N] == False:
    time += 1
    for _ in range(len(cases)):
        now = cases.popleft()
        if 0 < now:
            append_case(now-1)
        if now < 100000:
            append_case(now+1)
        if visited[N]:
            break
print(time)