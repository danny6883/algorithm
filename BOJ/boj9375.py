import sys
read = sys.stdin.readline

for _ in range(int(read())):
    cloth = dict()
    case = 1
    for i in range(int(read())):
        name, kind = read().rstrip().split()
        if kind in cloth.keys():
            cloth[kind] += 1
        else:
            cloth[kind] = 1
    for value in cloth.values():
        case *= value + 1
    print(case-1)