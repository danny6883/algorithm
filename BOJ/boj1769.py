X = int(input())
cnt = 0
while X >= 10:
    temp = 0
    for i in str(X):
        temp += int(i)
    X = temp
    cnt += 1
print(cnt)
if X in (3,6,9):
    print("YES")
else:
    print("NO")