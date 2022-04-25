board = [[0]*100 for _ in range(100)]
size = 0
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            if board[i][j] == 0:
                board[i][j] = 1
                size += 1
print(size)