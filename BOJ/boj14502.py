import sys, itertools
read = sys.stdin.readline

N, M = map(int, read().split())
board = [list(map(int, read().split())) for _ in range(N)]
virus = []
blank = []
direct = [(0,-1),(0,1),(-1,0),(1,0)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            blank.append((i,j))
        elif board[i][j] == 2:
            virus.append((i,j))

def virus_spread(i,j):
    for dx, dy in direct:
        if 0 <= i+dx < N and 0 <= j+dy < M and temp[i+dx][j+dy] == 0:
            temp[i+dx][j+dy] += 3
            virus_spread(i+dx,j+dy)

ans = 0
for comb in itertools.combinations(blank,3):
    temp = [board[i][:] for i in range(N)]
    temp_ans = 0
    for i,j in comb:
        temp[i][j] = 1
    for i,j in virus:
        virus_spread(i,j)
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                temp_ans += 1
    ans = max(ans, temp_ans)
print(ans)