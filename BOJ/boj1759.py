import itertools
L, C = map(int, input().split())
chars = input().split()
chars.sort()
vowel = ['a', 'e', 'i', 'o', 'u']
vo = []
co = []
ans = []
for c in chars:
    if c in vowel:
        vo.append(c)
    else:
        co.append(c)
for i in range(1,L-1):
    for v in itertools.combinations(vo,i):
        for c in itertools.combinations(co,L-i):
            temp = ''
            vi = 0
            ci = 0
            while vi < i and ci < L-i:
                if v[vi] < c[ci]:
                    temp += v[vi]
                    vi += 1
                else:
                    temp += c[ci]
                    ci += 1
            while vi < i:
                temp += v[vi]
                vi += 1
            while ci < L-i:
                temp += c[ci]
                ci += 1
            ans.append(temp)
ans.sort()
print('\n'.join(ans))