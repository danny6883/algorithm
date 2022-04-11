import sys
read = sys.stdin.readline

N, K = map(int, read().split())
nations = [list(map(int, read().split())) for _ in range(N)]
i = 0
while nations[i][0] != K:
    i += 1
gold, silver, bronze = nations[i][1:]
cnt = 1
for t1, t2, t3, t4 in nations:
    if t2 > gold:
        cnt += 1
    elif t2 == gold:
        if t3 > silver:
            cnt += 1
        elif t3 == silver:
            if t4 > bronze:
                cnt += 1
print(cnt)