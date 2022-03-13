import sys, collections
read = sys.stdin.readline
ans = []
for _ in range(int(read())):
    input_key = read().rstrip()
    left = []
    right = collections.deque()
    for k in input_key:
        if k == '<':
            if left:
                right.appendleft(left.pop())
        elif k == '>':
            if right:
                left.append(right.popleft())
        elif k == '-':
            if left:
                left.pop()
        else:
            left.append(k)
    ans.append(''.join(left+list(right)))
print('\n'.join(ans))