n = int(input())
an = list(map(int, input().split()))
cal = list(map(int, input().split()))
min = 1000000000
max = -1000000000
idx = 1

def calc(res):
    global min
    global max
    global idx

    if sum(cal) == 0:
        if min > res:
            min = res
        if max < res:
            max = res
        return

    if cal[0]:
        temp = res + an[idx]
        cal[0] -= 1
        idx += 1
        calc(temp)
        cal[0] += 1
        idx -= 1
    if cal[1]:
        temp = res - an[idx]
        cal[1] -= 1
        idx += 1
        calc(temp)
        cal[1] += 1
        idx -= 1
    if cal[2]:
        temp = res * an[idx]
        cal[2] -= 1
        idx += 1
        calc(temp)
        cal[2] += 1
        idx -= 1
    if cal[3]:
        temp = res // an[idx]
        if res < 0 and res % an[idx] != 0:
            temp += 1
        cal[3] -= 1
        idx += 1
        calc(temp)
        cal[3] += 1
        idx -= 1

calc(an[0])

print(max)
print(min)