n = int(input())
a = []
for i in range(n):
    a.append(tuple(map(int, input().split())))

a.sort(key = lambda k:k[0])
a.sort(key = lambda k:k[1])

min = a[0][0]
cnt = 0

for i in range(n):
    if min <= a[i][0]:
        min = a[i][1]
        cnt += 1

print(cnt)