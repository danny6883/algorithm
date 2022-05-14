A, B = map(int, input().split())
if abs(A) > abs(B):
    temp = A
    A = B
    B = temp
if A < 0:
    sum_A = -A*(A-1)//2
else:
    sum_A = A*(A+1)//2
if B < 0:
    sum_B = -B*(B-1)//2
else:
    sum_B = B*(B+1)//2
if A * B < 0:
    print(sum_B + sum_A)
else:
    print(sum_B - sum_A + A)
