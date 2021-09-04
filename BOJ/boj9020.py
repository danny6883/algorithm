import sys
read = sys.stdin.readline

prime = [False, False, True] + [True, False]*5000
le = len(prime)
for i in range(3, le, 2):
    a = 2
    while le > i*a:
        prime[i*a] = False
        a += 1

ans = ''
t = int(read())
for _ in range(t):
    n = int(read())
    first = n // 2
    if first != 2 and first % 2 == 0:
        first -= 1
    while True:
        if prime[first] and prime[n-first]:
            ans += str(first) + ' ' + str(n-first) + '\n'
            break
        if first == 3:
            first = 2
        else:
            first -= 2
print(ans, end='')