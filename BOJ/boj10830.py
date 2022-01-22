import sys
read = sys.stdin.readline

n, b = map(int, read().split())
a = []
for _ in range(n):
    a.append(list(map(int, read().split())))
for x in range(n):
    for y in range(n):
        a[x][y] %= 1000

def matmul(mat1, mat2):
    n = len(mat1)
    matmul_a = [[0 for i in range(n)] for j in range(n)]
    for x in range(n):
        for z in range(n):
            for y in range(n):
                matmul_a[x][z] += mat1[x][y] * mat2[y][z]
            matmul_a[x][z] %= 1000
    return matmul_a

def power(mat,p):
    if p == 1:
        return a
    temp = power(mat,p//2)
    if p % 2 == 0:
        return matmul(temp,temp)
    else:
        return matmul(matmul(temp,temp),a)

mat = []
mat = a[:]
mat = power(mat,b)
for row in mat:
    print(' '.join(map(str,row)))