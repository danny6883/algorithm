w = [[[0 for i in range(21)] for j in range(21)] for k in range(21)]

def wf(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if w[a][b][c] != 0:
        return w[a][b][c]
    if a < b and b < c:
        return wf(a, b, c-1) + wf(a, b-1, c-1) - wf(a, b-1, c)
    return wf(a-1, b, c) + wf(a-1, b-1, c) + wf(a-1, b, c-1) - wf(a-1, b-1, c-1)

for i in range(21):
    for j in range(21):
        for k in range(21):
            w[i][j][k] = wf(i, j, k)

while(1):
    abc = list(map(int, input().split()))
    if abc[0] == -1 and abc[1] == -1 and abc[2] == -1:
        break
    if abc[0] <= 0 or abc[1] <= 0 or abc[2] <= 0:
        print("w("+str(abc[0])+", "+str(abc[1])+", "+str(abc[2])+") = 1")
        continue
    if abc[0] > 20 or abc[1] > 20 or abc[2] > 20:
        print("w("+str(abc[0])+", "+str(abc[1])+", "+str(abc[2])+") = 1048576")
        continue
    print("w("+str(abc[0])+", "+str(abc[1])+", "+str(abc[2])+") = "+str(w[abc[0]][abc[1]][abc[2]]))