n = int(input())
n1 = 1
n2 = 2
mod = 10007
for i in range((n-1)//2):
    n1 = (n1+n2)%mod
    n2 = (n1+n2)%mod
if n%2 == 1:
    print(n1)
else:
    print(n2)