case = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0:
        break
    print('Case {}: '.format(case), end='')
    case += 1
    if V%P < L:
        print(V//P*L + V%P)
    else:
        print(V//P*L + L)