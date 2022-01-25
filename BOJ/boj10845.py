import collections, sys
read = sys.stdin.readline

queue_x = collections.deque()
ans = []
for _ in range(int(read())):
    order = read().rstrip().split()
    if order[0] == 'push':
        queue_x.append(int(order[1]))
    elif order[0] == 'pop':
        ans.append(queue_x.popleft() if queue_x else -1)
    elif order[0] == 'size':
        ans.append(int(len(queue_x)))
    elif order[0] == 'empty':
        ans.append(0 if queue_x else 1)
    elif order[0] == 'front':
        ans.append(queue_x[0] if queue_x else -1)
    else:
        ans.append(queue_x[-1] if queue_x else -1)
print('\n'.join(map(str,ans)))