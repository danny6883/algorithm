import sys
read = sys.stdin.readline

N, M, B = map(int, read().split())
land = [list(map(int, read().split())) for _ in range(N)]
left = 0
right = 256

def is_flat(height):
    inventory = B
    for row in land:
        for data in row:
            inventory += data - height
    if inventory >= 0:
        return True
    else:
        return False

def time(height):
    t = 0
    for row in land:
        for data in row:
            temp = data - height
            if temp > 0:
                t += temp*2
            else:
                t += -temp
    return t

def search(left, right):
    if left <= right:
        global ans
        mid = (left + right) // 2
        if is_flat(mid):
            ans = mid
            if time(mid) >= time(mid+1):
                search(mid+1,right)
            else:
                search(left,mid-1)
        else:
            search(left,mid-1)

ans = 0
search(left,right)
t = time(ans)

t_minus1 = 0
t_plus1 = 0
if is_flat(ans-1):
    t_minus1 = time(ans-1)
    if t >= t_minus1:
        t_minus1 = 0
if is_flat(ans+1):
    t_plus1 = time(ans+1)
    if t < t_plus1:
        t_plus1 = 0
if t_minus1 and t_minus1 < t and (t_plus1 == 0 or t_minus1 < t_plus1):
    print(t_minus1,ans-1)
elif t_plus1 and t_plus1 <= t:
    print(t_plus1,ans+1)
else:
    print(t,ans)