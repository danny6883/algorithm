import sys
read = sys.stdin.readline

xy = list()
for _ in range(int(read())):
    xy.append(tuple(map(int, read().split())))
xy.sort(key = lambda k: k[0])
xy.sort(key = lambda k: k[1])
for dot in xy:
    print(' '.join(map(str,dot)))