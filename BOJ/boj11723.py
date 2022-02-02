import sys
read = sys.stdin.readline

S = set()
M = int(read())
for _ in range(M):
    order = read().rstrip().split()
    if order[0] == 'add':
        S.add(int(order[1]))
    elif order[0] == 'remove':
        try:
            S.remove(int(order[1]))
        except:
            pass
    elif order[0] == 'check':
        if int(order[1]) in S:
            print('1')
        else:
            print('0')
    elif order[0] == 'toggle':
        try:
            S.remove(int(order[1]))
        except:
            S.add(int(order[1]))
    elif order[0] == 'all':
        S = {i for i in range(1,21)}
    else:
        S = set()