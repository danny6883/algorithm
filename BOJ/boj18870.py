N = int(input())
inp = list(map(int, input().split()))
sx = list()
out = []
for n, xn in enumerate(inp):
    sx.append([n, xn])
sx.sort(key = lambda k: k[1])
count = 0
press = [0]
for i in range(1, N):
    if sx[i-1][1] != sx[i][1]:
        count += 1
    press.append(count)
for i in range(0, N):
    sx[i][1] = press[i]
sx.sort(key = lambda k: k[0])
for i in range(0, N):
    out.append(str(sx[i][1]))
print(' '.join(out))