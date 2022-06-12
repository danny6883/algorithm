import sys, heapq
read = sys.stdin.readline

N = int(read())
cards = [int(read()) for _ in range(N)]
heapq.heapify(cards)
ans = 0
for _ in range(N-1):
  first = heapq.heappop(cards)
  second = heapq.heappop(cards)
  ans += first + second
  heapq.heappush(cards, first + second)
print(ans)
