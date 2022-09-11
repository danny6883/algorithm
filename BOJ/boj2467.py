N = int(input())
values = list(map(int, input().split()))

left = 0
right = N - 1

while True:
    if left > right:
        mid = left
        break
    mid = (left+right)//2
    if values[mid] < 0:
        left = mid + 1
    else:
        right = mid - 1

lp = mid - 1
rp = mid
min_sum = abs(values[0] + values[1])
ans = [values[0], values[1]]
if mid == N:
    ans = values[N-2], values[N-1]

if min_sum > abs(values[mid-2] + values[mid-1]):
    min_sum = abs(values[mid-2] + values[mid-1])
    ans = [values[mid-2], values[mid-1]]
if mid+1 < N and min_sum > abs(values[mid] + values[mid+1]):
    min_sum = abs(values[mid] + values[mid+1])
    ans = [values[mid], values[mid+1]]

while lp >= 0 and rp < N and min_sum != 0:
    if min_sum > abs(values[lp] + values[rp]):
        min_sum = abs(values[lp] + values[rp])
        ans = [values[lp], values[rp]]
    if abs(values[lp]) > abs(values[rp]):
        rp += 1
    else:
        lp -= 1
print(*ans)