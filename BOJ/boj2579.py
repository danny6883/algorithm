import sys
read = sys.stdin.readline

stairs = []
n = int(read())
for _ in range(n):
    stairs.append(int(read()))

scores = [[0,0,0]]
for i in range(1,n+1):
    scores.append([max(scores[i-1][1:]),scores[i-1][0]+stairs[i-1],scores[i-1][1]+stairs[i-1]])
print(max(scores[n][1:]))