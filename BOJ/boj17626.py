N = int(input())
squares = []
i = 1
while i**2 <= N:
    squares.append(i**2)
    i += 1
find = False
cnt = 1
if squares[-1] == N:
    find = True
len_sq = len(squares)
while cnt < 4 and find == False:
    if cnt == 2:
        for x in range(len_sq):
            for y in range(x,len_sq):
                if squares[x]+squares[y] == N:
                    find = True
                    break
                elif squares[x]+squares[y] > N:
                    break
            if find:
                break
        if find:
            break
    if find:
        break
    if cnt == 3:
        for x in range(len_sq):
            for y in range(x,len_sq):
                for z in range(y,len_sq):
                    if squares[x]+squares[y]+squares[z] == N:
                        find = True
                        break
                    elif squares[x]+squares[y]+squares[z] > N:
                        break
                if find:
                    break
            if find:
                break
        if find:
            break
    if find:
        break
    cnt += 1
print(cnt)