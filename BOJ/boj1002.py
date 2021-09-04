import sys, math
read = sys.stdin.readline

for _ in range(int(read())):
    x1, y1, r1, x2, y2, r2 = map(int, read().split())
    dist = math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2))
    if dist == 0 and r1 == r2:
        print(-1)
    elif dist > r1 + r2:
        print(0)
    elif dist == r1 + r2:
        print(1)
    elif dist < r1 + r2 and dist >= max(r1, r2):
        print(2)
    elif dist < max(r1, r2) and abs(r1-r2) < dist:
        print(2)
    elif abs(r1-r2) == dist:
        print(1)
    elif abs(r1-r2) > dist:
        print(0)