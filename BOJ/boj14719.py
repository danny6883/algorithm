H, W = map(int, input().split())
heights = list(map(int, input().split()))
ans = 0

left = heights[0]
max_height = max(heights)
for i in range(W-1,-1,-1):
    if heights[i] == max_height:
        rightmost_highest = i
        break
for i in range(1,rightmost_highest+1):
    if left > heights[i]:
        ans += left - heights[i]
    elif left < heights[i]:
        left = heights[i]

right = heights[W-1]
for i in range(W-1,rightmost_highest,-1):
    if right > heights[i]:
        ans += right - heights[i]
    elif right < heights[i]:
        right = heights[i]

print(ans)