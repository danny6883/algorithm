import sys
read = sys.stdin.readline

stack = []
for _ in range(int(read())):
    order = read().strip()
    if order[:3] == 'pus':
        stack.append(int(order[5:]))
    elif order[:3] == 'pop':
        if len(stack) == 0:
            print('-1')
        else:
            print(stack.pop())
    elif order[:3] == 'siz':
        print(len(stack))
    elif order[:3] == 'emp':
        if len(stack) > 0:
            print('0')
        else:
            print('1')
    else:
        if len(stack) == 0:
            print('-1')
        else:
            print(stack[-1])