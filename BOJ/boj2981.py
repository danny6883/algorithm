import sys
read = sys.stdin.readline

n = int(read())
m = []
ans = []
for _ in range(n):
    m.append(int(read()))
m.sort()
dist = m[1] - m[0]
for i in range(2,n):
    if dist > m[i] - m[i-1]:
        dist = m[i] - m[i-1]
div1 = []
div2 = [dist]
for i in range(2, int(dist**(0.5))+1):
    if dist % i == 0:
        div1.append(i)
        if i**2 != dist:
            div2.append(dist // i)
div = div1 + div2[::-1]
for i in div:
    ism = 1
    temp = m[0] % i
    for mi in m:
        if temp != mi % i:
            ism = 0
            break
    if ism:
        ans.append(i)
print(' '.join(map(str,ans)))