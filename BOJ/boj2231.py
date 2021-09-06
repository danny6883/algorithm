n = str(input())
ans = False
for i in range(-9*len(n),1):
    out = int(n) + i
    if out <= 0:
        continue
    if out + sum(map(int, str(out))) == int(n):
        ans = True
        break
if ans:
    print(out)
else:
    print(0)