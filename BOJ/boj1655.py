import heapq, sys
read = sys.stdin.readline

ans = []
left = []
len_left = 1
right = []
len_right = 0

N = int(read())
left.append(-int(read()))
ans.append(str(-left[0]))
for i in range(N-1):
    num = int(read())
    if num <= -left[0]:
        heapq.heappush(left,-num)
        len_left += 1
    else:
        heapq.heappush(right,num)
        len_right += 1

    if len_left < len_right:
        heapq.heappush(left,-heapq.heappop(right))
        len_right -= 1
        len_left += 1
    if len_left > len_right + 1:
        heapq.heappush(right,-heapq.heappop(left))
        len_right += 1
        len_left -= 1
    ans.append(str(-left[0]))
print('\n'.join(ans))