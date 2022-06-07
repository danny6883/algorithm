import collections
paren = collections.deque(input())

def open_paren():
    global err
    if len(paren) >= 2 and paren[0] == '(' and paren[1] == ')':
        paren.popleft()
        paren.popleft()
        return 2 + open_paren()
    if len(paren) >= 2 and paren[0] == '[' and paren[1] == ']':
        paren.popleft()
        paren.popleft()
        return 3 + open_paren()
    if not paren:
        if stack:
            err = True
        return 0

    now = paren.popleft()
    if now == '(':
        stack.append(now)
        return 2 * open_paren() + open_paren()
    elif now == '[':
        stack.append(now)
        return 3 * open_paren() + open_paren()
    elif now == ')':
        if stack == []:
            paren.clear()
            err = True
            return 0

        if stack.pop() == '(':
            return 0
        else:
            paren.clear()
            err = True
            return 0
    elif now == ']':
        if stack == []:
            paren.clear()
            err = True
            return 0

        if stack.pop() == '[':
            return 0
        else:
            paren.clear()
            err = True
            return 0
    else:
        paren.clear()
        err = True
        return 0
ans = 0
stack = []
err = False
while paren:
    ans += open_paren()
    if err:
        ans = 0
        break
print(ans)