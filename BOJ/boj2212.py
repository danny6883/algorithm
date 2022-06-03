N = int(input())
K = int(input())
sensor = list(map(int, input().split()))
ans = 0
if N > K:
    sensor.sort()
    dist = [(sensor[i+1] - sensor[i],i) for i in range(N-1)]
    dist.sort(reverse = True)
    cut = [-1]
    for i in range(K-1):
        cut.append(dist[i][1])
    cut.sort()
    for i in range(K-1):
        ans += sensor[cut[i+1]] - sensor[cut[i]+1]
    ans += sensor[-1] - sensor[cut[K-1]+1]
print(ans)