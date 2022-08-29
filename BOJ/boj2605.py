N = int(input())
nums = list(map(int, input().split()))
ans = []
for i in range(N):
    ans = ans[:nums[i]] + [i+1] + ans[nums[i]:]
print(*reversed(ans))