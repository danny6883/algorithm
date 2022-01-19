import sys
read = sys.stdin.readline

n = int(read())
series = []
for _ in range(n):
    series.append(int(read()))

pos = True
stack = [0]
ans = []
temp = [i for i in range(n,0,-1)]
for i in range(n):
    while stack[-1] < series[i]:
        stack.append(temp.pop())
        ans.append('+')
    ans.append('-')
    if stack.pop() != series[i]:
        pos = False
        break
if pos:
    print('\n'.join(ans))
else:
    print("NO")