n = int(input())
m = int(input())
over = 10**9
costs = [[over]*n for _ in range(n)]
for i in range(n):
    costs[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    if costs[a-1][b-1] > c:
        costs[a-1][b-1] = c
for k in range(n):
    for i in range(n):
        for j in range(n):
            if costs[i][j] > costs[i][k] + costs[k][j]:
                costs[i][j] = costs[i][k] + costs[k][j]
for i in range(n):
    for j in range(n):
        if costs[i][j] >= over:
            costs[i][j] = 0
for i in range(n):
    print(*costs[i])