N = int(input())
cards = list(map(int, input().split()))
for i in range(1,N):
    for j in range((i+1)//2):
        cards[i] = max(cards[i], cards[j]+cards[i-j-1])
print(cards[N-1])