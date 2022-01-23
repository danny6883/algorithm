import sys
read = sys.stdin.readline

k, n = map(int,read().split())
lan = []
for _ in range(k):
    lan.append(int(read()))
left = 1
right = 2**32-1
while left <= right:
    mid = (left + right) // 2
    temp_n = 0
    for l in lan:
        temp_n += l // mid
    if temp_n < n:
        right = mid - 1
    else:
        left = mid + 1
        ans = mid
print(ans)