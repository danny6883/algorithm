import itertools

mod = 10007
n = int(input())
factorial = [1]
temp = 1
for i in range(1,n+1):
    temp *= i
    factorial.append(temp)
plus_square2m1 = n%2
case = 0
comb = itertools.combinations(range(n//2+2),2)
for idx in comb:
    square2m1 = 2*idx[0] + plus_square2m1
    square1m2 = idx[1] - idx[0] - 1
    square2m2 = (n//2+2) - idx[1] - 1
    case += factorial[square2m1+square1m2+square2m2] // factorial[square2m1] // factorial[square1m2] // factorial[square2m2] % mod
print(case%mod)