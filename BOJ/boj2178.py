import sys
read = sys.stdin.readline

def put_queue(x,y):
    if 0 <= x < N and 0 <= y < M and visit[x][y] == 0 and miro[x][y] == '1':
        temp.add((x,y))
        visit[x][y] += 1

N, M = map(int, read().split())
miro = [read().rstrip() for _ in range(N)]
queue = [(0,0)]
visit = [[0 for i in range(M)] for j in range(N)]
cnt = 0

while True:
    cnt += 1
    if (N-1,M-1) in queue:
        break
    temp = set()
    for x,y in queue:
        visit[x][y] += 1
        put_queue(x-1,y)
        put_queue(x+1,y)
        put_queue(x,y-1)
        put_queue(x,y+1)
    queue = list(temp)
print(cnt)