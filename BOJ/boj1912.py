n = int(input())
seq = list(map(int, input().split()))

total = []
total.append([seq[0],seq[0]])
for i in range(1,n):
    total.append([max(total[i-1]),max(total[i-1][1]+seq[i],seq[i])])
print(max(total[-1]))