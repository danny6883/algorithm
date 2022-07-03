N = int(input())
dist = list(map(int, input().split()))
dist.sort()
print(dist[(N-1)//2])