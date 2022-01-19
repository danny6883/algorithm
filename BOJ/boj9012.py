import sys
read = sys.stdin.readline

for _ in range(int(read())):
    open = 0
    vps = True
    ps = read().rstrip()
    for p in ps:
        if p == '(':
            open += 1
        else:
            open -= 1
            if open < 0:
                vps = False
                break
    if open == 0 and vps:
        print("YES")
    else:
        print("NO")