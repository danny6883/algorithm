import sys, collections
read = sys.stdin.readline

N = int(read())
board = [list(map(int, read().split())) for _ in range(N)]
cases = [[0]*(N+9) for _ in range(N+9)]

cases[N-1][N-1] = 1

for k in range(1,N):
    for i in range(k+1):
        x, y = N-1-(k-i), N-1-i
        cases[x][y] += cases[x][y+board[x][y]] + cases[x+board[x][y]][y]
x = 0
y = N-2
for k in range(N-2,-1,-1):
    x = 0
    y = k
    while y >= 0:
        cases[x][y] += cases[x][y+board[x][y]] + cases[x+board[x][y]][y]
        x += 1
        y -= 1

print(cases[0][0])