import sys
read = sys.stdin.readline

N = int(read())
cards = dict()
for _ in range(N):
    num = int(read())
    if num in cards:
        cards[num] += 1
    else:
        cards[num] = 1

max_cnt = 0
ans = 0
for num, cnt in cards.items():
    if max_cnt < cnt:
        max_cnt = cnt
        ans = num
    elif max_cnt == cnt:
        if ans > num:
            ans = num
print(ans)