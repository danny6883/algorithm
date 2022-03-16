import sys
read = sys.stdin.readline

ans = []
for _ in range(int(read())):
    N = int(read())
    scores = []
    for i in range(N):
        scores.append(list(map(int,read().split())))
    scores.sort()
    high_score = scores[0][1]
    cnt = 1
    for i in range(1,N):
        if scores[i][1] < high_score:
            cnt += 1
            high_score = scores[i][1]
    ans.append(str(cnt))
print('\n'.join(ans))