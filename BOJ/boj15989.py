import sys
read = sys.stdin.readline

cases = [[1,0,0] for _ in range(10001)]
cases[1] = [1,0,0]
cases[2] = [1,1,0]
cases[3] = [1,1,1]
for i in range(4,10001):
    cases[i][1] = sum(cases[i-2][:2])
    cases[i][2] = sum(cases[i-3])

T = int(read())
ans = []
for _ in range(T):
    n = int(read())
    ans.append(str(sum(cases[n])))
print('\n'.join(ans))