import sys, itertools
read = sys.stdin.readline

N, M = map(int, read().split())
no_mix = dict()
for i in range(1,N+1):
    no_mix[i] = []
for _ in range(M):
    fir, sec = map(int, read().split())
    no_mix[fir].append(sec)
    no_mix[sec].append(fir)
combinations = itertools.combinations(range(1,N+1),3)
ans = 0
for comb in combinations:
    if comb[1] in no_mix[comb[0]] or comb[2] in no_mix[comb[0]] or comb[1] in no_mix[comb[2]]:
        continue
    ans += 1
print(ans)