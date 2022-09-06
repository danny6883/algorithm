import sys
read = sys.stdin.readline

N, M = map(int, read().split())
friends = dict()
for i in range(N):
    friends[i] = []
for _ in range(M):
    a, b = map(int, read().split())
    friends[a].append(b)
    friends[b].append(a)

def find(i, cnt, visited):
    if cnt >= 5:
        return True
    for neighbor in friends[i]:
        if neighbor in visited:
            continue
        if find(neighbor, cnt+1, visited.union({neighbor})):
            return True
    return False

flag = 0
for i in range(N):
    if find(i,1,{i}):
        flag = 1
        break
print(flag)