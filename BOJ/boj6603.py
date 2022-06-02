import sys, itertools
read = sys.stdin.readline

ans = []
while True:
    case = list(map(int, read().split()))
    if case[0] == 0:
        break
    k = case[0]
    S = case[1:]
    for comb in itertools.combinations(S,6):
        ans.append(' '.join(map(str, comb)))
    ans.append('')
print('\n'.join(ans))