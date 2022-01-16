import sys
read = sys.stdin.readline

n = int(read())
line = []
for _ in range(n):
    line.append(list(map(int, read().split())))
line.sort(key = lambda k: k[0])
b_line = []
for i in range(n):
    b_line.append(line[i][1])

length = [0]*n
length[0] = 1
for i in range(1,n):
    max_length = 0
    for index in range(i):
        if b_line[i] > b_line[index] and max_length < length[index]:
            max_length = length[index]
    length[i] = max_length + 1
print(n - max(length))