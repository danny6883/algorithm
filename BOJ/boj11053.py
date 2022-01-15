n = int(input())
a = list(map(int, input().split()))
lis = []
lis.append(a[0])
i = 1
while i < n:
    if lis[-1] < a[i]:
        lis.append(a[i])
        i += 1
    elif lis[-1] > a[i]:
        small = 1
        while i+small >= n or lis[-1] > a[i+small]:
            small += 1
            
print(len(lis))