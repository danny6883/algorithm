import sys
read = sys.stdin.readline

num = list()
for _ in range(int(read())):
    num.append(int(read()))
num.sort()
for i in num:
    print(i)