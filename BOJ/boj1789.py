def bs(left, right):
    if left > right:
        return left
    mid = (left+right)//2
    if mid*(mid+1)//2 <= S:
        if left==right:
            return left
        return bs(mid+1,right)
    else:
        if left==right:
            return left-1
        return bs(left,mid-1)

S = int(input())
print(bs(1,int((S*2)**0.5)))