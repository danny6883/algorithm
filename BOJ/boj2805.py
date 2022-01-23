n, m = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = 10**9

while left <= right:
    mid = (left + right) // 2
    temp = 0
    for tree in trees:
        if tree - mid > 0:
            temp += tree - mid
    if temp < m:
        right = mid - 1
    else:
        left = mid + 1
        ans = mid
print(ans)