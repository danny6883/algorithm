n, m = map(int, input().split())
find = list(map(int, input().split()))

count = 0
queue_x = [i for i in range(1,n+1)]
length = n

for find_x in find:
    for i in range(length):
        if queue_x[i] == find_x:
            index = i
            break
    if length - index < index:
        count += length - index
    else:
        count += index
    if index + 1 >= length:
        queue_x = queue_x[:index]
    else:
        queue_x = queue_x[index+1:] + queue_x[:index]
    length -= 1
print(count)