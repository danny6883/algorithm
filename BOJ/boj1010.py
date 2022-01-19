import sys
read = sys.stdin.readline

com = [[] for _ in range(30)]
com[0].append(1)
for i in range(1,30):
  com[i].append(1)
  for j in range(1,i):
    com[i].append(com[i-1][j-1]+com[i-1][j])
  com[i].append(1)

for _ in range(int(read())):
  n, m = map(int, read().split())
  print(com[m][n])