import sys
read = sys.stdin.readline

ans = []
for _ in range(int(read())):
    M, N, x, y = map(int, read().split())
    cnt = -1
    temp = (y-x)%N
    for i in range(N):
        if (M*i)%N == temp:
            cnt = M*i+x
            break
    ans.append(str(cnt))
print('\n'.join(ans))