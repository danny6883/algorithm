import sys, heapq, itertools
read = sys.stdin.readline

N, M = map(int, read().split())
city = [list(map(int, read().split())) for _ in range(N)]
homes = []
chickens = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            homes.append((i,j))
        elif city[i][j] == 2:
            chickens.append((i,j))
homes_dist = [[] for _ in range(len(homes))]
for i in range(len(homes)):
    for j in range(len(chickens)):
        heapq.heappush(homes_dist[i],(abs(chickens[j][0]-homes[i][0])+abs(chickens[j][1]-homes[i][1]), j))

ans = 10**9
for comb in itertools.combinations([i for i in range(len(chickens))], M):
    temp_ans = 0
    for j in range(len(homes)):
        temp_homes_dist = homes_dist[j][:]
        temp_dist, temp_index = heapq.heappop(temp_homes_dist)
        while temp_index not in comb:
            temp_dist, temp_index = heapq.heappop(temp_homes_dist)
        temp_ans += temp_dist
    ans = min(ans, temp_ans)
print(ans)