n = int(input())
i = 2
while n != 1 and i <= n:
    if n % i == 0:
        n = n // i
        print(i)
    else:
        i += 1