n, m = map(int, input().split())
if n-m < m:
    m = n-m
comb = [[],[1,1]]
for i in range(2,n+1):
    temp = [1]
    for j in range(1,i):
        if j > m:
            break
        temp.append(comb[i-1][j-1] + comb[i-1][j])
    temp.append(1)
    comb.append(temp)
print(comb[n][m])