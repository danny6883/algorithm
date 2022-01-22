n = int(input())
mod = 1000000007
a = [[1,1],[1,0]]

def matmul(mat1, mat2):
    n = len(mat1)
    matmul_a = [[0 for i in range(2)] for j in range(2)]
    for x in range(2):
        for z in range(2):
            for y in range(2):
                matmul_a[x][z] += mat1[x][y] * mat2[y][z]
            matmul_a[x][z] %= mod
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
mat = power(mat,n)
print(mat[0][1])