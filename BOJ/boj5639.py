import sys, bisect
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

nums = []
while True:
    try:
        nums.append(int(read()))
    except:
        break
ans = []

def postorder(start,end):
    if start >= end:
        return
    mid = bisect.bisect(nums,nums[start],start,end)
    postorder(start+1,mid)
    postorder(mid,end)
    ans.append(nums[start])

postorder(0,len(nums))
print('\n'.join(map(str,ans)))