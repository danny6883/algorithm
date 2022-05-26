import sys
read = sys.stdin.readline

board = [list(map(int, read().split())) for _ in range(19)]
visited = [[False]*19 for _ in range(19)]
winner = 0
stone = [-1,-1]

if winner == 0:
    dx, dy = 0, 1
    temp = 0
    x = temp
    while x < 19 - dx*4:
        y = 0
        while y < 19 - dy*4:
            if board[x][y]:
                color = board[x][y]
                cnt = 0
                while x < 19 and y < 19 and board[x][y] == color:
                    x += dx
                    y += dy
                    cnt += 1
                if cnt == 5:
                    winner = color
                    stone = [x - dx*5, y - dy*5]
                    break
            if x < 19 and y < 19 and board[x][y] == 0:
                x += dx
                y += dy
        if winner:
            break
        temp += 1
        x = temp

if winner == 0:
    dx, dy = 1, 0
    temp = 0
    y = temp
    while y < 19 - dy*4:
        x = 0
        while x < 19 - dx*4:
            if board[x][y]:
                color = board[x][y]
                cnt = 0
                while x < 19 and y < 19 and board[x][y] == color:
                    x += dx
                    y += dy
                    cnt += 1
                if cnt == 5:
                    winner = color
                    stone = [x - dx*5, y - dy*5]
                    break
            if x < 19 and y < 19 and board[x][y] == 0:
                x += dx
                y += dy
        if winner:
            break
        temp += 1
        y = temp

if winner == 0:
    dx, dy = 1, 1
    temp = 0
    y = temp
    while y < 19 - dy*4 and winner == 0:
        x = 0
        while x < 19 and y < 19:
            if board[x][y]:
                color = board[x][y]
                cnt = 0
                while x < 19 and y < 19 and board[x][y] == color:
                    x += dx
                    y += dy
                    cnt += 1
                if cnt == 5:
                    winner = color
                    stone = [x - dx*5, y - dy*5]
                    break
            if x < 19 and y < 19 and board[x][y] == 0:
                x += dx
                y += dy
        temp += 1
        y = temp

    temp = 1
    x = temp
    while x < 19 - dx*4 and winner == 0:
        y = 0
        while x < 19 and y < 19:
            if board[x][y]:
                color = board[x][y]
                cnt = 0
                while x < 19 and y < 19 and board[x][y] == color:
                    x += dx
                    y += dy
                    cnt += 1
                if cnt == 5:
                    winner = color
                    stone = [x - dx*5, y - dy*5]
                    break
            if x < 19 and y < 19 and board[x][y] == 0:
                x += dx
                y += dy
        temp += 1
        x = temp

if winner == 0:
    dx, dy = -1, 1
    temp = -dx*4
    x = temp
    while x < 19 and winner == 0:
        y = 0
        while x < 19 and y < 19:
            if board[x][y]:
                color = board[x][y]
                cnt = 0
                while x < 19 and y < 19 and board[x][y] == color:
                    x += dx
                    y += dy
                    cnt += 1
                if cnt == 5:
                    winner = color
                    stone = [x - dx*5, y - dy*5]
                    break
            if x < 19 and y < 19 and board[x][y] == 0:
                x += dx
                y += dy
        temp += 1
        x = temp

    temp = 0
    y = temp
    while y < 19 - dy*4 and winner == 0:
        x = 18
        while x < 19 and y < 19:
            if board[x][y]:
                color = board[x][y]
                cnt = 0
                while x < 19 and y < 19 and board[x][y] == color:
                    x += dx
                    y += dy
                    cnt += 1
                if cnt == 5:
                    winner = color
                    stone = [x - dx*5, y - dy*5]
                    break
            if x < 19 and y < 19 and board[x][y] == 0:
                x += dx
                y += dy
        temp += 1
        y = temp

if winner:
    print(winner)
    print(stone[0]+1, stone[1]+1)
else:
    print(winner)