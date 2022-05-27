N = int(input())
i = 1
ans = 0
while N > 0:
    temp = 9*(10**(i-1))
    ans += min(N,temp)*i
    N -= temp
    i += 1
print(ans)