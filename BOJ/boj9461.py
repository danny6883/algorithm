p = [0] * 100
p[0] = 1
p[1] = 1
p[2] = 1
p[3] = 2
p[4] = 2
for i in range(5, 100):
    p[i] = p[i-1] + p[i-5]
for _ in range(int(input())):
    print(p[int(input())-1])