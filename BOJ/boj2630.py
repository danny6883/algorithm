import sys
read = sys.stdin.readline

n = int(read())
paper_ = []
for _ in range(n):
    paper_.append(list(map(int, read().split())))
    
def cut(paper, white, blue):
    if len(paper) == 1:
        if paper[0][0]:
            blue += 1
        else:
            white += 1
        return [white, blue]
    same = True
    for colors in paper:
        for color in colors:
            if color != paper[0][0]:
                same = False
                break
        if same == False:
            break
    if same:
        if paper[0][0]:
            blue += 1
        else:
            white += 1
        return [white, blue]

    white_plus = 0
    blue_plus = 0
    temp_paper = []
    for i in range(len(paper)//2):
        temp_paper.append(paper[i][:len(paper)//2])
    temp = cut(temp_paper, white, blue)
    white_plus += temp[0]
    blue_plus += temp[1]

    temp_paper = []
    for i in range(len(paper)//2):
        temp_paper.append(paper[i][len(paper)//2:])
    temp = cut(temp_paper, white, blue)
    white_plus += temp[0]
    blue_plus += temp[1]

    temp_paper = []
    for i in range(len(paper)//2,len(paper)):
        temp_paper.append(paper[i][:len(paper)//2])
    temp = cut(temp_paper, white, blue)
    white_plus += temp[0]
    blue_plus += temp[1]

    temp_paper = []
    for i in range(len(paper)//2,len(paper)):
        temp_paper.append(paper[i][len(paper)//2:])
    temp = cut(temp_paper, white, blue)
    white_plus += temp[0]
    blue_plus += temp[1]

    return [white + white_plus, blue + blue_plus]
print('\n'.join(map(str, cut(paper_,0,0))))