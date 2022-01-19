n = int(input())
A = list(map(int, input().split()))

nge = [-1 for _ in range(n)]
stack = [(0,A[0])]

for i in range(1,n):
    while stack and stack[-1][1] < A[i]:
        nge[stack.pop()[0]] = A[i]
    stack.append((i,A[i]))
print(*nge)