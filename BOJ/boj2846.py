N = int(input())
heights = list(map(int, input().split()))
heights.append(0)
low = heights[0]
ans = 0
i = 1
while i < N:
    if heights[i] >= heights[i+1]:
        if ans < heights[i] - low:
            ans = heights[i] - low
        low = heights[i+1]
    i += 1
print(ans)