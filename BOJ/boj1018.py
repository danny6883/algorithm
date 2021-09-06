import sys
read = sys.stdin.readline

n, m = map(int, read().split())
board = [['W' for i in range(m)] for j in range(n)]
ans = 64
for i in range(n):
    board[i] = list(read().rstrip())
for x in range(n-7):
    for y in range(m-7):
        first = 'W'
        second = 'B'
        draw = 0
        for a in range(8):
            if draw > ans:
                    break
            for b in range(8):
                if draw > ans:
                    break
                if (a%2==0) == (b%2==0):
                    if board[x+a][y+b] != first:
                        draw += 1
                else:
                    if board[x+a][y+b] != second:
                        draw += 1
        if ans > draw:
            ans = draw
            
        first = 'B'
        second = 'W'
        draw = 0
        for a in range(8):
            if draw > ans:
                    break
            for b in range(8):
                if draw > ans:
                    break
                if (a%2==0) == (b%2==0):
                    if board[x+a][y+b] != first:
                        draw += 1
                else:
                    if board[x+a][y+b] != second:
                        draw += 1
        if ans > draw:
            ans = draw
print(ans)