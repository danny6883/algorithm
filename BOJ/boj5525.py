N = int(input())
M = int(input())
S = input()
PN = 'I'+'OI'*N
cnt = 0
index = -1

while True:
    temp = index
    index = S[index+1:].find(PN)
    if index == -1:
        break
    index += temp+1
    cnt += 1
    while True:
        if S[index+2*N+1:index+2*N+3] == 'OI':
            index += 2
            cnt += 1
        else:
            index += 2*N
            break
print(cnt)