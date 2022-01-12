n = int(input())
count = [0]+[1]*9
for _ in range(1,n):
    temp = [0]*10
    temp[1] += count[0]
    for i in range(1,9):
        temp[i-1] += count[i]
        temp[i+1] += count[i]
    temp[8] += count[9]
    count = temp[:]
print(sum(count)%1000000000)