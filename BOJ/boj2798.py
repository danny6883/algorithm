n, m = map(int, input().split())
cards = list(map(int, input().split()))
out = set()
for a in range(0, n-2):
    for b in range(a+1, n-1):
        for c in range(b+1, n):
            out.add(cards[a] + cards[b] + cards[c])
out = list(out)
out.sort()
ans = out[-1]
for i in range(len(out)):
    if out[i] > m:
        ans = out[i-1]
        break
print(ans)