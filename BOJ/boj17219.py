import sys
read = sys.stdin.readline

N, M = map(int, read().split())
sites = dict()
for _ in range(N):
    address, password = read().split()
    sites[address] = password
ans = []
for _ in range(M):
    address = read().rstrip()
    ans.append(sites[address])
print('\n'.join(ans))