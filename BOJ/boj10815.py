input()
card_N = list(map(int,input().split()))
input()
card_M = list(map(int,input().split()))
ans = []
hand_card = dict()
for card in card_N:
    hand_card[card] = 1
for card in card_M:
    if card in hand_card:
        ans.append(1)
    else:
        ans.append(0)
print(*ans)