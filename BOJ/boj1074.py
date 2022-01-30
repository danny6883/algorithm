N, r, c = map(int, input().split())
# N1 = [[0,1],[2,3]]
# plus = 4
# for _ in range(N-1):
#     for row in N1:
#         row += [i+plus for i in row]
#     plus *= 2
#     temp = []
#     for row in N1:
#         temp.append([i+plus for i in row])
#     N1 += temp
#     plus *= 2
# print(N1[r][c])

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

# def sqrt2(i):
#     n = 2
#     while True:
#         if i < n:
#             break
#         n *= 2
#     return n ** 2

# def search(x,y):
#     # if 
#     if x > y:
#         return sqrt2(x) - 1 - search(y,x)