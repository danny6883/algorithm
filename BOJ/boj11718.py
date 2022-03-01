import sys
ans = []
while True:
    input_str = sys.stdin.readline().rstrip()
    if input_str:
        ans.append(input_str)
    else:
        break
print('\n'.join(ans))