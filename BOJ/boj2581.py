m = int(input())
n = int(input())
prime = list()
for i in range(m, n+1):
    p = True
    for a in range(2, int(i**0.5+1)):
        if i % a == 0:
            p = False
            break
    if i == 1:
        pass
    elif i == 2 or p:
        prime.append(i)
if prime:
    print(sum(prime))
    print(prime[0])
else:
    print(-1)