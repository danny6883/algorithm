N = int(input())
nums = list(map(int, input().split()))
ans = 0
bigger = True
smaller = True
cnt = 1
same = 0
for i in range(1,N):
    if nums[i-1] < nums[i]:
        smaller = False
        if bigger:
            cnt += 1
        else:
            ans = max(ans, cnt)
            bigger = True
            cnt = 2 + same
        same = 0
    elif nums[i-1] > nums[i]:
        bigger = False
        if smaller:
            cnt += 1
        else:
            ans = max(ans, cnt)
            smaller = True
            cnt = 2 + same
        same = 0
    else:
        same += 1
        cnt += 1
ans = max(ans, cnt)
print(ans)