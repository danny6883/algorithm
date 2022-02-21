import sys
read = sys.stdin.readline

T = int(read())
ans = []
for _ in range(T):
    n = int(read())
    stickers = [list(map(int, read().split())) for i in range(2)]
    if n == 1:
        ans.append(str(max(stickers[0][-1], stickers[1][-1])))
        continue
    scores = [[0]*n for i in range(2)]
    scores[0][0] = stickers[0][0]
    scores[0][1] = stickers[1][0] + stickers[0][1]
    scores[1][0] = stickers[1][0]
    scores[1][1] = stickers[0][0] + stickers[1][1]
    for i in range(2,n):
        scores[0][i] = max(scores[1][i-2], scores[1][i-1]) + stickers[0][i]
        scores[1][i] = max(scores[0][i-2], scores[0][i-1]) + stickers[1][i]
    ans.append(str(max(scores[0][-1], scores[1][-1])))
print('\n'.join(ans))