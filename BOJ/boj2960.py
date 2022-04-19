N, K = map(int, input().split())
now = 2
prime = [True]*(N+1)
prime[0] = False
prime[1] = False
cnt = 0
ans = 0

while ans == 0:
    while prime[now] == False:
        now += 1
    for i in range(1,N//now+1):
        if prime[now*i]:
            prime[now*i] = False
            cnt += 1
            if cnt == K:
                ans = now*i
                break
print(ans)