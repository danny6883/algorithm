n = int(input())
out = 1
for i in range(1, n+1):
    out *= i
if n == 0:
    print(1)
else:
    print(out)