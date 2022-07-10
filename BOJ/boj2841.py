import sys
read = sys.stdin.readline

N, P = map(int, read().split())
stack = [[] for _ in range(7)]
ans = 0
for _ in range(N):
    line, fret = map(int, read().split())
    while stack[line] != [] and stack[line][-1] > fret:
        ans += 1
        stack[line].pop()
    if stack[line] and stack[line][-1] == fret:
        continue
    stack[line].append(fret)
    ans += 1
print(ans)