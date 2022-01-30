N, r, c = map(int, input().split())

def cube4(n,x,y):
    if x <= 1 and y <= 1:
        return 2*x+y
    half_length = 2**(n-1)
    if half_length > x:
        if half_length > y:
            return cube4(n-1,x,y)
        else:
            return 4**(n-1) + cube4(n-1,x,y-half_length)
    else:
        return 4**(n-1)*2 + cube4(n,x-half_length,y)
print(cube4(N,r,c))