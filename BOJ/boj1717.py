import sys
read = sys.stdin.readline

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    
    if height[a] > height[b]:
        parent[b] = a
    else:
        if height[a] == height[b]:
            height[b] += 1
        parent[a] = b

n, m = map(int, read().split())
parent = [i for i in range(n+1)]
height = [1 for i in range(n+1)]
ans = []
for _ in range(m):
    f, a, b = map(int, read().split())
    if f == 0:
        if a == b:
            continue
        union(a,b)
    elif f == 1:
        if a == b or find(a) == find(b):
            ans.append('YES')
        else:
            ans.append('NO')
print('\n'.join(ans))