N = int(input())
res = [' '*i for i in range(N-1,-1,-1)]
stars = ['*','* *','*****']
while len(stars) <= N:
    len_stars = len(stars)
    temp = []
    for i in range(len_stars):
        temp.append(stars[i] + ' '*len(stars[-1-i]) + stars[i])
    stars += temp
for i in range(N):
    res[i] += stars[i] + res[i]
print('\n'.join(res))