N = int(input())
MOD = 10007
nn = [1]*10
for j in range(N-1):
    last = sum(nn) % MOD
    for i in range(10):
        temp = nn[i]
        nn[i] = last
        last -= temp
print(sum(nn) % MOD)