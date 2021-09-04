input()
a = list(map(int, input().split()))
count = 0
for num in a:
    prime = True
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            prime = False
            break
    if num == 1:
        pass
    elif num == 2 or prime:
        count += 1
print(count)