import sys
read = sys.stdin.readline

ans = []
for _ in range(int(read())):
    p = read().rstrip()
    n = int(read())
    if n == 0:
        read()
        xn = []
    else:
        xn = list(map(int, read().rstrip()[1:-1].split(',')))
    left = 1
    popleft = 0
    popright = 0
    for func in p:
        if func == 'R':
            left = (left+1)%2
        elif func == 'D':
            if left:
                popleft += 1
            else:
                popright += 1
    if popleft + popright > n:
        ans.append('error')
        continue
    if popright:
        xn = xn[popleft:-popright]
    else:
        xn = xn[popleft:]
    if left == 0:
        xn.reverse()
    ans.append('[' + ','.join(map(str,xn)) + ']')
print('\n'.join(ans))