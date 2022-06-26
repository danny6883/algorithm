N, L = map(int, input().split())
loc = list(map(int, input().split()))
loc.sort()
ans = 0
last = -L
for i in range(N):
    if loc[i] >= last + L:
        ans += 1
        last = loc[i]
print(ans)