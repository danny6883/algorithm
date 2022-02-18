import sys
read = sys.stdin.readline

mod = 1000000007
M = int(read())
sum = 0
for _ in range(M):
    N, S = map(int, read().split())
    sum = (sum + S * pow(N,mod-2,mod)) % mod
print(sum)