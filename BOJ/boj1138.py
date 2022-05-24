N = int(input())
left_many = list(map(int, input().split()))
line = [0]*N
for i in range(N):
    cnt = 0
    temp = 0
    while cnt < left_many[i]:
        if line[temp] == 0:
            cnt += 1
        temp += 1
    while line[temp] != 0:
        temp += 1
    line[temp] = i+1
print(*line)