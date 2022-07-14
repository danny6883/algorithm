import sys
read = sys.stdin.readline

R, C, T = map(int, read().split())
room = [list(map(int, read().split())) for _ in range(R)]
dir = [(0,-1),(0,1),(-1,0),(1,0)]
cleaner = 2
for i in range(R):
    if room[i][0] == -1:
        cleaner = i
        break

next = [row[:] for row in room]
for _ in range(T):
    for i in range(R):
        for j in range(C):
            if room[i][j] >= 5:
                amount = room[i][j] // 5
                for dx,dy in dir:
                    if 0 <= i+dx < R and 0 <= j+dy < C and not ((i+dx == cleaner or i+dx == cleaner+1) and j+dy == 0):
                        next[i][j] -= amount
                        next[i+dx][j+dy] += amount

    for i in range(cleaner-1,0,-1):
        next[i][0] = next[i-1][0]
    for j in range(C-1):
        next[0][j] = next[0][j+1]
    for i in range(cleaner):
        next[i][C-1] = next[i+1][C-1]
    for j in range(C-1,1,-1):
        next[cleaner][j] = next[cleaner][j-1]
    next[cleaner][1] = 0

    cleaner += 1
    for i in range(cleaner+1,R-1):
        next[i][0] = next[i+1][0]
    for j in range(C-1):
        next[R-1][j] = next[R-1][j+1]
    for i in range(R-1,cleaner,-1):
        next[i][C-1] = next[i-1][C-1]
    for j in range(C-1,1,-1):
        next[cleaner][j] = next[cleaner][j-1]
    next[cleaner][1] = 0
    cleaner -= 1

    room = [row[:] for row in next]
print(sum([sum(row) for row in room])+2)