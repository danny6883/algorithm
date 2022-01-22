import sys
read = sys.stdin.readline

n = int(read())
paper = []
for _ in range(n):
    paper.append(list(map(int, read().split())))

minus_one = 0
zero = 0
one = 0

def cut(paper):
    global minus_one, zero, one
    same = True
    for row in paper:
        for data in row:
            if data != paper[0][0]:
                same = False
                break
        if same == False:
            break
    if same:
        if paper[0][0] == -1:
            minus_one += 1
        elif paper[0][0] == 0:
            zero += 1
        else:
            one += 1
        return
    
    size = len(paper)

    for x in range(3):
        for y in range(3):
            temp_paper = []
            for i in range(size//3*x,size//3*(x+1)):
                temp_paper.append(paper[i][size//3*y:size//3*(y+1)])
            cut(temp_paper)

cut(paper)
print(minus_one)
print(zero)
print(one)