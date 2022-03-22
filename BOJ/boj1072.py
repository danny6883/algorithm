X, Y = map(int, input().split())
Z = int(Y*100/X)

def bs(left, right):
    if left >= right:
        return left
    mid = (left+right)//2
    if int((Y+mid)*100/(X+mid)) == Z:
        return bs(mid+1,right)
    else:
        return bs(left,mid)
if Z == 99 or Z == 100:
    print(-1)
else:
    print(bs(1,X))