import sys
sys.setrecursionlimit(10**8)
n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
out = 0
case = 0
y_range = [i for i in range(n)]
def queen(case):
    if case == n:
        global out
        out += 1
        return
    x = case
    for y in y_range:
        if x == 0:
            if y == n // 2:
                out *= 2
                if n%2 == 0:
                    return
            elif y == n // 2 + 1:
                return
        if board[x][y] == 0:
            y_range.remove(y)
            for i in range(1,min(n-x,y+1)):
                board[x+i][y-i] += 1
            for i in range(1,min(n-x,n-y)):
                board[x+i][y+i] += 1
            case += 1
            queen(case)
            case -= 1
            if len(y_range) == 0 or y_range[-1] < y:
                y_range.append(y)
            else:
                for i in range(len(y_range)):
                    if y_range[i] > y:
                        y_range.insert(i,y)
                        break
            for i in range(1,min(n-x,y+1)):
                board[x+i][y-i] -= 1
            for i in range(1,min(n-x,n-y)):
                board[x+i][y+i] -= 1
queen(case)
print(out)