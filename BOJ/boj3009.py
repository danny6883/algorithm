x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
if x1==x2:
    print(x3, end=' ')
elif x2==x3:
    print(x1, end=' ')
else:
    print(x2, end=' ')
if y1==y2:
    print(y3)
elif y2==y3:
    print(y1)
else:
    print(y2)