while 1:
    n = list(map(int, input().split()))
    if n[0] == 0:
        break
    if n[1] % n[0] == 0:
        print("factor")
    elif n[0] % n[1] == 0:
        print("multiple")
    else:
        print("neither")