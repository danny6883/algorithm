import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

N = int(read())
regions = [list(map(int, read().split())) for _ in range(N)]
max_height = 0
for row in regions:
    max_height = max(max_height, max(row))
answer = 1

def safe(r,c):
    visited[r][c] = True
    for dx, dy in [(0,-1),(0,1),(-1,0),(1,0)]:
        if 0 <= r+dx < N and 0 <= c+dy < N and visited[r+dx][c+dy] == False and regions[r][c] > rain:
            safe(r+dx,c+dy)

for rain in range(1,max_height):
    safe_area_cnt = 0
    visited = [[False]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if visited[r][c] == False and regions[r][c] > rain:
                safe_area_cnt += 1
                safe(r,c)
    answer = max(answer, safe_area_cnt)
print(answer)