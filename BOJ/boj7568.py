import sys
read = sys.stdin.readline

n = int(read())
hw = list()
ans = list()
for _ in range(n):
    hw.append(tuple(map(int, read().split())))
for i in range(n):
    rank = 1
    for j in range(n):
        if hw[j][0] > hw[i][0] and hw[j][1] > hw[i][1]:
            rank += 1
    ans.append(str(rank))
print(' '.join(ans))