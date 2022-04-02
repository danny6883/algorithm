min_odd = 100
sum = 0
for _ in range(7):
    num = int(input())
    if num%2:
        if min_odd > num:
            min_odd = num
        sum += num
if sum:
    print(sum)
    print(min_odd)
else:
    print(-1)