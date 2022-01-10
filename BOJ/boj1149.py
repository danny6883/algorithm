import sys
read = sys.stdin.readline

n = int(read())
rgb = []
for _ in range(n):
    rgb.append(list(map(int, read().split())))
memo = []
memo.append(rgb[0])
for i in range(1,n):
    temp = []
    temp.append(rgb[i][0]+min(memo[i-1][1], memo[i-1][2]))
    temp.append(rgb[i][1]+min(memo[i-1][0], memo[i-1][2]))
    temp.append(rgb[i][2]+min(memo[i-1][0], memo[i-1][1]))
    memo.append(temp)
print(min(memo[n-1]))