import sys
read = sys.stdin.readline

first = list(read().rstrip())
second = []
for _ in range(int(read())):
    order = read().split()
    if order[0] == 'L':
        if first:
            second.append(first.pop())
    elif order[0] == 'D':
        if second:
            first.append(second.pop())
    elif order[0] == 'B':
        if first:
            first.pop()
    elif order[0] == 'P':
        first.append(order[1])
print(''.join(first+second[::-1]))