A, B = input().split()
len_A = len(A)
len_B = len(B)
min_diff = 50
for i in range(len_B-len_A+1):
    temp_B = B[i:i+len_A]
    diff = 0
    for j in range(len_A):
        if A[j] != temp_B[j]:
            diff += 1
    if diff < min_diff:
        min_diff = diff
print(min_diff)