import sys
read = sys.stdin.readline

ans = []
while True:
    ps = read().rstrip()
    if ps == '.':
        break
    stack = [0]
    vps = True
    for p in ps:
        if p == '(' or p == '[':
            stack.append(p)
        elif p == ')':
            if stack.pop() != '(':
                vps = False
                break
        elif p == ']':
            if stack.pop() != '[':
                vps = False
                break
    if stack[:] == [0] and vps:
        ans.append("yes")
    else:
        ans.append("no")
print('\n'.join(ans))