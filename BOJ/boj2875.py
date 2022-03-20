N, M, K = map(int, input().split())
if N//2 < M:
    cnt = N//2
    K -= M-N//2
else:
    cnt = M
    K -= N-2*M
if K > 0:
    cnt -= K//3
    if K%3:
        cnt -= 1
print(cnt)