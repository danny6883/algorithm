n, k = map(int, input().split())
ans = 1
if n < 2*k:
    k = n - k
for i in range(k):
    ans *= n-i
for i in range(k):
    ans //= k-i
print(ans)