import sys
read = sys.stdin.readline

n = int(read())
layer = []
for _ in range(n):
    layer.append(list(map(int, read().split())))
total = []
total.append(layer[0])
for i in range(1,n):
    temp = []
    temp.append(layer[i][0] + total[i-1][0])
    for j in range(1,i):
        temp.append(layer[i][j] + max(total[i-1][j-1], total[i-1][j]))
    temp.append(layer[i][i] + total[i-1][i-1])
    total.append(temp)
print(max(total[n-1]))