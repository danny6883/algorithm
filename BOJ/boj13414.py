import sys
read = sys.stdin.readline

K, L = map(int, read().split())
cnt = dict()
num = [0]*L
ans = []
len_ans = 0
for i in range(L):
    num[i] = read().rstrip()
    if num[i] in cnt:
        cnt[num[i]] += 1
    else:
        cnt[num[i]] = 1
for i in range(L):
    if cnt[num[i]] == 1:
        ans.append(num[i])
        len_ans += 1
        if len_ans == K:
            break
    else:
        cnt[num[i]] -= 1
print('\n'.join(map(str,ans)))