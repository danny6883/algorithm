import sys, collections
read = sys.stdin.readline

deque_x = collections.deque()
ans = []
for _ in range(int(read())):
    order = read().split()
    if order[0] == 'push_front':
        deque_x.appendleft(int(order[1]))
    elif order[0] == 'push_back':
        deque_x.append(int(order[1]))
    elif order[0] == 'pop_front':
        if deque_x:
            ans.append(deque_x.popleft())
        else:
            ans.append(-1)
    elif order[0] == 'pop_back':
        if deque_x:
            ans.append(deque_x.pop())
        else:
            ans.append(-1)
    elif order[0] == 'size':
        ans.append(len(deque_x))
    elif order[0] == 'empty':
        if deque_x:
            ans.append(0)
        else:
            ans.append(1)
    elif order[0] == 'front':
        if deque_x:
            ans.append(deque_x[0])
        else:
            ans.append(-1)
    else:
        if deque_x:
            ans.append(deque_x[-1])
        else:
            ans.append(-1)
print('\n'.join(map(str,ans)))