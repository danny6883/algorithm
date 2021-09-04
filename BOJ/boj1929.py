m, n = map(int, input().split())
for i in range(m, n+1):
    if i == 2:
        print(i)
        continue
    elif i % 2 == 0:
        continue
    p = True
    for d in range(2, int(i**0.5+1)):
        if i % d == 0:
            p = False
            break
    if i == 1:
        pass
    elif i == 2 or p:
        print(i)