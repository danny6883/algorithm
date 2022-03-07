import sys
read = sys.stdin.readline

N = int(read())
ropes = [int(read()) for _ in range(N)]
ropes.sort()
max_weight = 0
for i in range(N):
    if max_weight < ropes[i] * (N-i):
        max_weight = ropes[i] * (N-i)
print(max_weight)