import sys
read = sys.stdin.readline

ans = []
prime = [True]*1000001
for i in range(2,1001):
    if prime[i] == False:
        continue
    j = 2
    while i*j <= 1000000:
        prime[i*j] = False
        j += 1
prime[0] = False
prime[1] = False
prime[2] = False

prime_odd = []
for i in range(len(prime)):
    if prime[i]:
        prime_odd.append(i)

while True:
    n = int(read())
    if n == 0:
        break
    find = False
    for p in prime_odd:
        if p*2 > n:
            break
        if prime[n-p]:
            find = True
            ans.append('{0} = {1} + {2}'.format(n,p,n-p))
            break
    if find == False:
        ans.append("Goldbach's conjecture is wrong.")
print('\n'.join(ans))