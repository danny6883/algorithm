import sys, collections
read = sys.stdin.readline

T = int(read())
ans = []
move = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1)]
for _ in range(T):
    l = int(read())
    start = list(map(int, read().split()))
    end = list(map(int, read().split()))
    visit = [[0 for i in range(l)] for j in range(l)]
    visit[start[0]][start[1]] = 1
    cnt = 0
    find = False
    queue = collections.deque([start])
    while queue:
        for i in range(len(queue)):
            x, y = queue.popleft()
            if x == end[0] and y == end[1]:
                find = True
                break
            for mx, my in move:
                if 0 <= x+mx < l and 0 <= y+my < l and visit[x+mx][y+my] == 0:
                    visit[x+mx][y+my] += 1
                    queue.append((x+mx,y+my))
        if find:
            break
        cnt += 1
    ans.append(cnt)
print('\n'.join(map(str,ans)))