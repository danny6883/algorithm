import sys
read = sys.stdin.readline

N = int(read())
road  = list(map(int, read().split()))
oil = list(map(int, read().split()))

min_oil = oil[0]
price = 0
for i in range(N-1):
    price += road[i] * min_oil
    if min_oil > oil[i+1]:
        min_oil = oil[i+1]
print(price)