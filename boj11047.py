n, k = map(int, input().split())
i = 0
coin = []
for i in range(n):
    coin.append(int(input()))

cnt = 0
while k > 0:
    cnt += k // coin[i]
    k = k % coin[i]
    i = i - 1

print(cnt)