N, K = map(int, input().split())
max = 100000
visit = [0]*100001
queue = [N]
time = 0
find = False
while True:
    temp = []
    for i in range(len(queue)):
        point = queue.pop(0)
        if point == K:
            find = True
            break
        if point-1 >= 0 and visit[point-1] == 0:
            queue.append(point-1)
            visit[point-1] += 1
        if point+1 <= 100000 and visit[point+1] == 0:
            queue.append(point+1)
            visit[point+1] += 1
        if point*2 <= 100000 and visit[point*2] == 0:
            queue.append(point*2)
            visit[point*2] += 1
    if find:
        break
    time += 1
print(time)