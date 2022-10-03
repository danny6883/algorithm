import sys
read = sys.stdin.readline

N, M = map(int, read().split())
r, c, d = map(int, read().split())
board = [list(map(int, read().split())) for _ in range(N)]
cleaned = [[False]*M for _ in range(N)]

direct = [(-1,0),(0,1),(1,0),(0,-1)]
answer = 0
cnt = 0
while True:
    if cleaned[r][c] == False:
        cleaned[r][c] = True
        answer += 1
        cnt = 0
    temp_r, temp_c = r+direct[d-1][0], c+direct[d-1][1]
    if board[temp_r][temp_c] == 0 and cleaned[temp_r][temp_c] == False:
        d = (d-1)%4
        r, c = temp_r, temp_c
        cnt = 0
    else:
        if cnt < 4:
            d = (d-1)%4
            cnt += 1
        else:
            r, c = r-direct[d][0], c-direct[d][1]
            cnt = 0
            if board[r][c]:
                break
print(answer)