import sys
read = sys.stdin.readline

M, N, K = map(int, read().split())
board = [[0]*N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, read().split())
    for y in range(y1,y2):
        for x in range(x1,x2):
            board[y][x] = 1

def dfs(r,c):
    area = 1
    stack = [(r,c)]
    board[r][c] = 1
    while stack:
        r_, c_ = stack.pop()
        for dr, dc in [(r_,c_-1),(r_,c_+1),(r_-1,c_),(r_+1,c_)]:
            if 0 <= dr < M and 0 <= dc < N and board[dr][dc] == 0:
                board[dr][dc] = 1
                area += 1
                stack.append((dr,dc))
    return area

results = []
for r in range(M):
    for c in range(N):
        if board[r][c] == 0:
            results.append(dfs(r,c))

results.sort()
print(len(results))
print(*results)