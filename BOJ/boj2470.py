N = int(input())
val = list(map(int, input().split()))
val.sort()
index = 0
while index < N:
    if val[index] >= 0:
        break
    index += 1

ans1, ans2 = val[index%N], val[(index+1)%N]
target = abs(val[index%N]+val[(index+1)%N])
if target > abs(val[index-1]+val[index-2]):
    target = abs(val[index-1]+val[index-2])
    ans1, ans2 = val[index-2], val[index-1]

left = index - 1
right = index
while 0 <= left and right < N:
    temp = val[left] + val[right]
    if target > abs(temp):
        target = abs(temp)
        ans1, ans2 = val[left], val[right]
    if temp > 0:
        left -= 1
    elif temp < 0:
        right += 1
    else:
        break
print(ans1, ans2)