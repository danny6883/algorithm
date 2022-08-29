import sys
read = sys.stdin.readline

N, M = map(int, read().split())
to_use = [int(read()) for _ in range(N)]

def wd(x):
    cnt = 0
    temp = 0
    for day in to_use:
        if day <= temp:
            temp -= day
        else:
            if day > x:
                return M+1
            cnt += 1
            temp = x - day
        if cnt > M:
            break
    return cnt
    

def bs(left, right):
    if left > right:
        return left
    mid = (left + right) // 2
    if wd(mid) > M:
        return bs(mid+1, right)
    else:
        return bs(left, mid-1)

print(bs(0,10000*N))