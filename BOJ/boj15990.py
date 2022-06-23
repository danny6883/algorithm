import sys
read = sys.stdin.readline
mod = 1000000009

tc = [[0,0,0] for _ in range(100001)]
tc[1] = [1,0,0]
tc[2] = [0,1,0]
tc[3] = [1,1,1]
tc[4] = [2,0,1]
tc[5] = [1,2,1]
tc[6] = [3,3,2]
for i in range(7,100001):
    tc[i][2] += (tc[i-3][0] + tc[i-3][1]) % mod
    tc[i][1] += (tc[i-2][0] + tc[i-2][2]) % mod
    tc[i][0] += (tc[i-1][1] + tc[i-1][2]) % mod
T = int(read())
ans = [sum(tc[int(read())]) % mod for _ in range(T)]
print('\n'.join(map(str,ans)))