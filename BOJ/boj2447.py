n = int(input())
stars = [[' ' for i in range(n)] for j in range(n)]
def star(x, y, k):
    if k == 1:
        stars[x][y] = '*'
    else:
        k = k // 3
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                else:
                    star(x+i*k, y+j*k, k)
star(0,0,n)
for i in range(len(stars)):
    for j in range(len(stars[i])):
        print(stars[i][j], end='')
    print()