import sys
read = sys.stdin.readline

N = int(read())
ans = list(read().rstrip())
len_file = len(ans)
for _ in range(N-1):
    file = read().rstrip()
    for i in range(len_file):
        if ans[i] != '?' and ans[i] != file[i]:
            ans[i] = '?'
print(''.join(ans))