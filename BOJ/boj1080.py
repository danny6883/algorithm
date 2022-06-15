from operator import xor
import sys
read = sys.stdin.readline

N, M = map(int, read().split())
mat_A = [read().rstrip() for _ in range(N)]
mat_B = [read().rstrip() for _ in range(N)]
mat_diff = [[mat_A[i][j] == mat_B[i][j] for j in range(M)] for i in range(N)]
ans = 0
for i in range(N-2):
    for j in range(M-2):
        if not mat_diff[i][j]:
            for x in range(i,i+3):
                for y in range(j,j+3):
                    mat_diff[x][y] = not mat_diff[x][y]
            ans += 1
for i in range(N):
    for j in range(M):
        if not mat_diff[i][j]:
            ans = -1
            break
    if ans == -1:
        break
print(ans)