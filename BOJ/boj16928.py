import sys, collections
read = sys.stdin.readline

N, M = map(int, read().split())
board = [0 for i in range(101)]
visited = [0 for i in range(106)]
visited[0] = 1
visited[1] = 1
visited[101] = 1
visited[102] = 1
visited[103] = 1
visited[104] = 1
visited[105] = 1
for i in range(N+M):
    start, end = map(int, read().split())
    board[start] = end
queue = collections.deque([1])
cnt = 0
while visited[100] == 0:
    for i in range(len(queue)):
        start = queue.popleft()
        for j in range(1,7):
            if visited[start+j] == 0:
                visited[start+j] += 1
                if board[start+j]:
                    if visited[board[start+j]] == 0:
                        visited[board[start+j]] += 1
                        queue.append(board[start+j])
                else:
                    queue.append(start+j)
    cnt += 1
print(cnt)