k = int(input())
signs = input().replace(' ','')

smaller = list(signs.split('>'))
max_f = ''
now = 9
for s in smaller:
    if s == '':
        max_f += str(now)
        now -= 1
    else:
        max_f += ''.join(map(str,[now - i for i in range(len(s),-1,-1)]))
        now -= len(s)+1
print(max_f)

bigger = list(signs.split('<'))
min_f = ''
now = 0
for s in bigger:
    if s == '':
        min_f += str(now)
        now += 1
    else:
        min_f += ''.join(map(str,[now + i for i in range(len(s),-1,-1)]))
        now += len(s)+1
print(min_f)