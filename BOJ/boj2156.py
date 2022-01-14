import sys
read = sys.stdin.readline

n = int(read())
amount = [0,0,0]
for i in range(1,n+1):
    grape = int(read())
    amount = [max(amount), amount[0]+grape, amount[1]+grape]
print(max(amount))