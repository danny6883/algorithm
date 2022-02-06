import sys
read = sys.stdin.readline

N, M = map(int, read().split())
nums = list(map(int, read().split()))
for i in range(1,N):
    nums[i] += nums[i-1]
sums = []
for _ in range(M):
    i, j = map(int, read().split())
    sums.append(str(nums[j-1] - nums[i-2] if i>1 else nums[j-1]))
print('\n'.join(sums))