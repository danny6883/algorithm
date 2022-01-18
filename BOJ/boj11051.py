n, k = map(int, input().split())
com = [[] for _ in range(n+1)]
com[0].append(1)
for i in range(1, n+1):
    com[i].append(1)
    for j in range(1,i):
        com[i].append((com[i-1][j-1]+com[i-1][j])%10007)
    com[i].append(1)
print(com[n][k])