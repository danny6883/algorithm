import sys
read = sys.stdin.readline

n = int(read())
ring = list(map(int, read().split()))
ans = []

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

for i in range(1, n):
    gcdi = gcd(ring[0], ring[i])
    ans.append(str(ring[0]//gcdi)+"/"+str(ring[i]//gcdi))
print("\n".join(ans))