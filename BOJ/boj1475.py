N = input()
nums = [0]*10
for num in N:
    nums[int(num)] += 1
nums[6] = (nums[6]+nums[9])//2 + (nums[6]+nums[9])%2
nums[9] = 0
print(max(nums))