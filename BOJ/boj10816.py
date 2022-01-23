n = int(input())
cards = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

count = dict()
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1
ans = []
for f in find:
    if f in count:
        ans.append(count[f])
    else:
        ans.append(0)
print(*ans)