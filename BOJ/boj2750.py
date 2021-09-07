import sys
read = sys.stdin.readline

n = int(read())
num = list()
for _ in range(n):
    num.append(int(read()))
num.sort()
for i in num:
    print(i)