import heapq
n, m = map(int, input().split())
cards = list(map(int, input().split()))
heapq.heapify(cards)

for _ in range(m):
    first = heapq.heappop(cards)
    second = heapq.heappop(cards)
    heapq.heappush(cards, first+second)
    heapq.heappush(cards, first+second)
print(sum(cards))