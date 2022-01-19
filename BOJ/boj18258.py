import collections, sys
deque_x = collections.deque()
read = sys.stdin.readline
for _ in range(int(read())):
    order = read().split()
    if order[0] == 'push':
        deque_x.append(int(order[1]))
    elif order[0] == 'pop':
        if deque_x:
            print(deque_x.popleft())
        else:
            print('-1')
    elif order[0] == 'size':
        print(len(deque_x))
    elif order[0] == 'empty':
        if deque_x:
            print('0')
        else:
            print('1')
    elif order[0] == 'front':
        if deque_x:
            print(deque_x[0])
        else:
            print('-1')
    else:
        if deque_x:
            print(deque_x[-1])
        else:
            print('-1')