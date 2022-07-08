import itertools
N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = sorted(list(set(comb for comb in itertools.combinations_with_replacement(nums,M))))
for arr in ans:
    print(*arr)