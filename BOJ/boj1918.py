equation = input()
stack = []
ans = ""
order = dict()
order['('] = -1
order[')'] = -1
order['*'] = 1
order['/'] = 1
order['+'] = 0
order['-'] = 0
for eq in equation:
    if ord('A') <= ord(eq) <= ord('Z'):
        ans += eq
    elif eq == '(':
        stack.append(eq)
    elif eq == ')':
        while True:
            temp = stack.pop()
            if temp == '(':
                break
            ans += temp
    else:
        while stack and order[stack[-1]] >= order[eq]:
            ans += stack.pop()
        stack.append(eq)
while stack:
    ans += stack.pop()
print(ans)