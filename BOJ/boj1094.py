import heapq
X = int(input())
sticks = [64]

while sum(sticks) > X:
    shortest = heapq.heappop(sticks)
    if sum(sticks) + shortest//2 < X:
        heapq.heappush(sticks,shortest//2)
    heapq.heappush(sticks,shortest//2)
print(len(sticks))