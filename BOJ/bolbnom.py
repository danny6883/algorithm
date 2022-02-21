N = int(input())
heights = list(map(int, input().split()))
max_height = heights[0]
for i in range(1,N-1):
    if heights[i-1] < heights[i+1]:
        if max_height < heights[i-1] + heights[i]:
            max_height = heights[i-1] + heights[i]
    else:
        if max_height < heights[i] + heights[i+1]:
            max_height = heights[i] + heights[i+1]
if max_height < heights[0]:
    max_height = heights[0]
if max_height < heights[-1]:
    max_height = heights[-1]
print(max_height)