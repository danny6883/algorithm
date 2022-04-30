resis = {'black':0,'brown':1,'red':2,'orange':3,'yellow':4,'green':5,'blue':6,'violet':7,'grey':8,'white':9}
ans = 0
for i in range(3):
    color = input()
    if i==0:
        ans += resis[color]
    elif i==1:
        ans *= 10
        ans += resis[color]
    else:
        ans *= 10**resis[color]
print(ans)