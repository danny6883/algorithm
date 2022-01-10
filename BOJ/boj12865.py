import sys
read = sys.stdin.readline

n, k = map(int, read().split())
wv = []
for _ in range(n):
    wv.append(list(map(int, read().split())))
total = [[0 for i in range(n+1)] for j in range(k+1)]
for i in range(1,k+1):
    for j in range(1,n+1):
        if wv[j-1][0] > i:
            total[i][j] = total[i][j-1]
        else:
            total[i][j] = max(total[i-wv[j-1][0]][j-1] + wv[j-1][1], total[i][j-1])
print(total[k][n])