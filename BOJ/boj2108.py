import sys
read = sys.stdin.readline

nums = list()
count = [0 for _ in range(8003)]
n = int(read())
for i in range(n):
    num = int(read())
    nums.append(num)
    count[num+4000] += 1
nums.sort()
print(round(sum(nums)/n))
print(nums[n//2])
max = max(count)
many = count.index(max)
try:
    sec = count[many+1:].index(max) + many + 1
    print(sec-4000)
except:
    print(many-4000)
print(nums[-1] - nums[0])