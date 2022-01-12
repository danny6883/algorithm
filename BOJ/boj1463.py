n = int(input())
count = 0
if n == 1:
    print("0")
else:
    ns = set()
    if n % 3 == 0:
        ns.add(n//3)
    if n % 2 == 0:
        ns.add(n//2)
    ns.add(n-1)
    while True:
        count += 1
        if 1 in ns:
            break
        temp = set()
        for x in ns:
            if x % 3 == 0:
                temp.add(x//3)
            if x % 2 == 0:
                temp.add(x//2)
            temp.add(x-1)
        ns = temp
    print(count)