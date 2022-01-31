import sys
read = sys.stdin.readline

M, N = map(int, read().split())
box = [list(map(int, read().split())) for _ in range(N)]

queue = []
unripe = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i,j))
        elif box[i][j] == 0:
            unripe += 1

def ripe(i,j):
    global unripe
    if 0 <= i < N and 0 <= j < M and box[i][j] == 0:
        box[i][j] += 1
        unripe -= 1
        temp_queue.append((i,j))

day = 0
while queue:
    if unripe <= 0:
        break
    day += 1
    temp_queue = []
    for start_i, start_j in queue:
        ripe(start_i+1,start_j)
        ripe(start_i-1,start_j)
        ripe(start_i,start_j+1)
        ripe(start_i,start_j-1)
    queue = temp_queue[:]
if unripe > 0:
    print(-1)
else:
    print(day)