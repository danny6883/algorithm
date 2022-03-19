import collections
N = int(input())
jump_nums = list(map(int, input().split()))
queue = collections.deque()
queue.append(0)
visited = [0]*(N+100)
visited[0] = 1
cnt = 0
while visited[N-1] == 0 and queue:
    temp = collections.deque()
    while queue:
        now = queue.popleft()
        if now + jump_nums[now] >= N-1:
            visited[N-1] = 1
            break
        for i in range(1,jump_nums[now]+1):
            if visited[now+i] == 0:
                visited[now+i] = 1
                temp.append(now+i)
    cnt += 1
    queue = temp
if visited[N-1]:
    print(cnt)
else:
    print(-1)