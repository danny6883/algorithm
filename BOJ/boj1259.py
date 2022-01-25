import sys
read = sys.stdin.readline

ans = []
while True:
    x = read().rstrip()
    if x == '0':
        break
    if x == x[::-1]:
        ans.append('yes')
    else:
        ans.append('no')
print('\n'.join(ans))