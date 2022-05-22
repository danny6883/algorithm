N = input()
M = int(input())
broken = []
unbroken = [str(i) for i in range(10)]
if M:
    broken = set(input().split())
    unbroken = []
    for i in [str(j) for j in range(10)]:
        if i not in broken:
            unbroken.append(i)
ans = abs(int(N)-100)

def can_press(channel):
    for c in channel:
        if c in broken:
            return False
    return True

def go_low(channel):
    for i in range(len(channel)):
        if channel[i] in broken:
            return str(int(str(int(channel[:i+1])-1) + unbroken[-1]*(len(channel)-1-i)))
    return channel

def go_high(channel):
    for i in range(len(channel)):
        if channel[i] in broken:
            return str(int(str(int(channel[:i+1])+1) + unbroken[0]*(len(channel)-1-i)))
    return channel

if unbroken:
    lowest = int(unbroken[0])
else:
    lowest = 987654321
if lowest <= int(N):
    low = go_low(N)
    while can_press(low) == False:
        low = go_low(low)
else:
    low = "987654321"

if unbroken == [] or unbroken == ['0']:
    high = "987654321"
else:
    high = go_high(N)
    while can_press(high) == False:
        high = go_high(high)

ans = min(ans, len(low)+abs(int(N)-int(low)), len(high)+abs(int(N)-int(high)))
print(ans)