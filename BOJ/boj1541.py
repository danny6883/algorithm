f = input().split('-')
result = 0
for i in range(len(f)):
    d = list(map(int, f[i].split('+')))
    for j in range(len(d)):
        if i == 0:
            result += int(d[j])
        else:
            result -= int(d[j])

print(result)