import sys
read = sys.stdin.readline

num = [0 for _ in range(10001)]
for _ in range(int(read())):
    num[int(read())] += 1
for n in range(len(num)):
    for count in range(num[n]):
        print(n)