import sys
read = sys.stdin.readline

def gcd(m, n):
    if n==0:
        return m
    return gcd(n, m%n)

for _ in range(int(read())):
    a, b = map(int, read().split())
    print(a*b//gcd(a,b))