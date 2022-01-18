N = int(input())
A = list(map(int, input().split()))

asc = [0]*N
asc[0] = 1
for i in range(1,N):
    max_length = 0
    for index in range(0,i):
        if A[i] > A[index] and max_length < asc[index]:
            max_length = asc[index]
        asc[i] = max_length + 1

A_rev = A[::-1]
desc = [0]*N
desc[0] = 1
for i in range(1,N):
    max_length = 0
    for index in range(0,i):
        if A_rev[i] > A_rev[index] and max_length < desc[index]:
            max_length = desc[index]
        desc[i] = max_length + 1
desc = desc[::-1]

total = [0]*N
for i in range(N):
    total[i] = asc[i] + desc[i]
print(max(total)-1)