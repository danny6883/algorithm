import sys
read = sys.stdin.readline

M, N, H = map(int, read().split())
box = [[list(map(int, read().split())) for i in range(N)] for j in range(H)]

queue = []
unripe = 0
for k in range(H):
    for i in range(N):
        for j in range(M):
            if box[k][i][j] == 1:
                queue.append((k,i,j))
            elif box[k][i][j] == 0:
                unripe += 1

def ripe(k,i,j):
    global unripe
    if 0 <= k < H and 0 <= i < N and 0 <= j < M and box[k][i][j] == 0:
        box[k][i][j] += 1
        unripe -= 1
        temp_queue.append((k,i,j))

day = 0
while queue:
    if unripe <= 0:
        break
    day += 1
    temp_queue = []
    for k,i,j in queue:
        ripe(k-1,i,j)
        ripe(k+1,i,j)
        ripe(k,i+1,j)
        ripe(k,i-1,j)
        ripe(k,i,j+1)
        ripe(k,i,j-1)
    queue = temp_queue[:]
if unripe > 0:
    print(-1)
else:
    print(day)