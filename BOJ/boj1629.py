a, b, c = map(int, input().split())

def mul(a,b,c):
    if b == 1:
        return a % c
    temp = mul(a,b//2,c)
    if b % 2 == 0:
        return temp * temp % c
    else:
        return temp * temp * a % c
print(mul(a,b,c))