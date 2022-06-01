heights = [int(input()) for _ in range(9)]
over = sum(heights) - 100
for i in range(9):
    if over - heights[i] in heights and over != 2 * heights[i]:
        temp = over - heights[i]
        heights.pop(i)
        heights.remove(temp)
        break
heights.sort()
print('\n'.join(map(str, heights)))