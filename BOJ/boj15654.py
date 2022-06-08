import itertools
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = []
for p in itertools.permutations(nums,M):
    ans.append(' '.join(map(str,p)))
print('\n'.join(ans))