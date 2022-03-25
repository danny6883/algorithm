N = int(input())
ans = []
for i in range(1,N+1):
    ans.append(' '*(N-i)+"*"*(2*i-1))
print('\n'.join(ans))