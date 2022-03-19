N = int(input())
ans = [" "*(N-1)+"*"]
for i in range(1,N-1):
    ans.append(" "*(N-1-i)+"*"+" "*(2*i-1)+"*")
if N > 1:
    ans.append("*"*(2*N-1))
print('\n'.join(ans))