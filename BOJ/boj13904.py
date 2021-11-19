import sys

assignment = []
for _ in range(int(sys.stdin.readline().strip())):
    d, w = map(int, sys.stdin.readline().split())
    assignment.append((d,w))
assignment.sort(key=lambda k:k[1], reverse=True)
do = [0]*1000
for i in assignment:
    for j in range(i[0]-1,-1,-1):
        if do[j] == 0:
            do[j] += i[1]
            break
print(sum(do))