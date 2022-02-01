import sys
read = sys.stdin.readline

N, M = map(int, read().split())
pocketmon = [read().rstrip() for _ in range(N)]
ans = []
for _ in range(M):
    Q = read().rstrip()
    if 48 <= ord(Q[0]) <= 57:
        ans.append(pocketmon[int(Q)-1])
    else:
        ans.append(str(pocketmon.index(Q)+1))
print('\n'.join(ans))