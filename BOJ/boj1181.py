import sys
read = sys.stdin.readline

inp = set()
n = int(read())
for _ in range(n):
    inp.add(str(read().rstrip()))
inp = list(inp)
inp.sort(key = lambda k: k)
inp.sort(key = lambda k: len(k))
print('\n'.join(inp))