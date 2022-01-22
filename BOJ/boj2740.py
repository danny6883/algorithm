import sys
read = sys.stdin.readline
n, m = map(int, read().split())
a = []
for _ in range(n):
    a.append(list(map(int, read().split())))
m, k = map(int, read().split())
b = []
for _ in range(m):
    b.append(list(map(int,read().split())))

ab = [[0 for i in range(k)] for j in range(n)]
for x in range(n):
    for z in range(k):
        for y in range(m):
            ab[x][z] += a[x][y] * b[y][z]

ans = []
for row in ab:
    ans.append(' '.join(map(str,row)))
print('\n'.join(ans))