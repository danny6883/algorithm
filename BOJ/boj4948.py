prime = [False, True] + [True, False]*123456
l = len(prime)
for i in range(3, int((123456*2)**0.5+1), 2):
    a = 2
    while l > i*a:
        prime[i*a-1] = False
        a += 1
while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in range(n+1, 2*n+1):
        count += int(prime[i-1])
    print(count)