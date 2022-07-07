import itertools
N, M = map(int, input().split())
nums = list(map(int, input().split()))
ans = sorted(list(set(per for per in itertools.permutations(nums,M))))
for arr in ans:
    print(*arr)