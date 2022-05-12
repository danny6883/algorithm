import sys
read = sys.stdin.readline

T = int(read())
for _ in range(T):
    cnt = 0
    x1, y1, x2, y2 = map(int, read().split())
    n = int(read())
    for i in range(n):
        Cx, Cy, r = map(int, read().split())
        if ((x1-Cx)**2 + (y1-Cy)**2 - r**2) * ((x2-Cx)**2 + (y2-Cy)**2 - r**2) < 0:
            cnt += 1
    print(cnt)