import collections
N, K = map(int, input().split())
visited = [False]*100001
case = [0]*100001
now = collections.deque([N])
visited[N] = True
case[N] = 1
time = 0
while case[K] == 0:
    for _ in range(len(now)):
        index = now.popleft()
        if 0 <= index-1 <= 100000 and visited[index-1] == False:
            now.append(index-1)
        if 0 <= index+1 <= 100000 and visited[index+1] == False and index+1 <= K:
            now.append(index+1)
        if 0 <= index*2 <= 100000 and visited[index*2] == False and index < K:
            now.append(index*2)
    for index in now:
        case[index] += 1
        visited[index] = True
    time += 1
print(time)
print(case[K])