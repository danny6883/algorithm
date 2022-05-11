import sys
read = sys.stdin.readline

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if heights[x] > heights[y]:
        parents[y] = x
    elif heights[y] > heights[x]:
        parents[x] = y
    else:
        heights[x] += 1
        parents[y] = x

N = int(read())
M = int(read())
parents = [i for i in range(N)]
heights = [0 for _ in range(N)]
for i in range(N):
    connect = list(map(int, read().split()))
    for j in range(N):
        if connect[j]:
            union(i,j)
ans = "YES"
plan = list(map(int, read().split()))
for i in range(M-1):
    if find(plan[i]-1) != find(plan[i+1]-1):
        ans = "NO"
        break
print(ans)