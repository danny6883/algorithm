N = int(input())
nums = list(map(int, input().split()))
nums.sort()
ans = 0
for i in range(N//2):
    ans += abs(nums[i]-nums[N-1-i])
for i in range((N-1)//2):
    ans += abs(nums[i+1]-nums[N-1-i])
if N%2:
    i = (N-1)//2-1
    if abs(nums[0]-nums[N//2]) > abs(nums[i+1]-nums[N-1-i]):
        ans -= abs(nums[i+1]-nums[N-1-i])
        ans += abs(nums[0]-nums[N//2])
else:
    i = N//2-1
    if abs(nums[0]-nums[N//2]) > abs(nums[i]-nums[N-1-i]):
        ans -= abs(nums[i]-nums[N-1-i])
        ans += abs(nums[0]-nums[N//2])
print(ans)