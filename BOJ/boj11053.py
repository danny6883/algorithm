n = int(input())
a = list(map(int, input().split()))
length = [0]*n
length[0] = 1
for i in range(1,n):
    max_length = 0
    for index in range(0,i):
        if a[i] > a[index] and max_length < length[index]:
            max_length = length[index]
    length[i] = max_length + 1
print(max(length))