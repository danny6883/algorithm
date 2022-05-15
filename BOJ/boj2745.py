N, B = input().split()
B = int(B)
ans = 0
for i in range(len(N)-1,-1,-1):
    if ord('0') <= ord(N[i]) <= ord('9'):
        ans += (B**(len(N)-1-i))*int(N[i])
    else:
        ans += (B**(len(N)-1-i))*(ord(N[i])-ord("A")+10)
print(ans)