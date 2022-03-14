day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
x, y = map(int, input().split())
y += (x-1)*31
if x > 11:
    y -= 7
elif x > 9:
    y -= 6
elif x > 6:
    y -= 5
elif x > 4:
    y -= 4
elif x > 2:
    y -= 3
print(day[y%7])