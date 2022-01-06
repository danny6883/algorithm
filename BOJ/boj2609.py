n, m = map(int, input().split())
if n > m:
    temp = n
    n = m
    m = temp
big = 1
i = 2
a = n
b = m
while 1:
    if a % i == 0 and b % i == 0:
        big *= i
        a = a // i
        b = b // i
    else:
        i += 1
    if i > a:
        break
print(big)
print(n*m//big)