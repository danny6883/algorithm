n, k  = map(int, input().split())
mod = 1000000007
ans = 1
for i in range(1,n+1):
    ans = ans * i % mod
temp = 1
for i in range(1,k+1):
    temp = temp * i % mod
for i in range(1,n-k+1):
    temp = temp * i % mod
ans = ans * pow(temp,mod-2,mod) % mod
print(ans)