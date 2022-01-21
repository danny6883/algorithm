import sys
read = sys.stdin.readline

n = int(read())
video = []
for _ in range(n):
    video.append(list(map(int, read().rstrip())))
ans = ''
def comp(quad):
    global ans
    same = True
    for row in quad:
        for data in row:
            if data != quad[0][0]:
                same = False
                break
        if same == False:
            break
    if same:
        ans += str(quad[0][0])
        return
    
    ans += '('
    quad_temp = []
    for row in quad[:len(quad)//2]:
        quad_temp.append(row[:len(quad)//2])
    comp(quad_temp)

    quad_temp = []
    for row in quad[:len(quad)//2]:
        quad_temp.append(row[len(quad)//2:])
    comp(quad_temp)

    quad_temp = []
    for row in quad[len(quad)//2:]:
        quad_temp.append(row[:len(quad)//2])
    comp(quad_temp)

    quad_temp = []
    for row in quad[len(quad)//2:]:
        quad_temp.append(row[len(quad)//2:])
    comp(quad_temp)
    ans += ')'
comp(video)
print(ans)