A, B = map(int, input().split())
if A == B:
    print(0)
else:
    if A > B:
        temp = A
        A = B
        B = temp
    AB = [i for i in range(A+1,B)]
    print(B-A-1)
    print(*AB)