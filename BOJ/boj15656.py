import collections
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = collections.deque([[n] for n in nums])
for i in range(M-1):
    for _ in range(len(ans)):
        now = ans.popleft()
        for n in nums:
            ans.append(now + [n])
for arr in ans:
    print(*arr)