import sys
read = sys.stdin.readline

mod = 1000000009
cases = [0,1,2,4]
temp = 3
for i in range(4,1000001):
    temp = (temp - cases[i-4] + cases[i-1]) % mod
    cases.append(temp)

ans = []
T = int(read())
for _ in range(T):
    n = int(read())
    ans.append(str(cases[n]))
print('\n'.join(ans))