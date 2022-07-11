import sys
read = sys.stdin.readline

prime = [False,True]*(1000001//2)
prime[1] = False
prime[2] = True
for i in range(3,1000001//2,2):
    if prime[i]:
        j = 3
        while i*j < 1000000:
            prime[i*j] = False
            j += 2

prime_nums = [i for i in range(3,1000001,2) if prime[i]]
ans = []
T = int(read())
for _ in range(T):
    N = int(read())
    temp = 0
    if N == 4:
        ans.append(1)
        continue
    for pn in prime_nums:
        if pn > N//2:
            break
        if prime[N - pn]:
            temp += 1
    ans.append(temp)
print('\n'.join(map(str,ans)))