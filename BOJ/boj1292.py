A, B = map(int, input().split())

first = 0
i = int((A*2)**0.5)
while i*(i+1)//2 < A:
    i += 1
for j in range(1,i):
    first += j*j
first += i*(A-(i-1)*i//2-1)

second = 0
i = int((B*2)**0.5)
while i*(i+1)//2 < B:
    i += 1
for j in range(1,i):
    second += j*j
second += i*(B-(i-1)*i//2)
print(second-first)