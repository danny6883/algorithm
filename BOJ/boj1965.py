n = int(input())
boxes = list(map(int, input().split()))
max_cnt = [1]*n
for i in range(n):
    for j in range(i-1,-1,-1):
        if boxes[j] < boxes[i]:
            max_cnt[i] = max(max_cnt[j]+1, max_cnt[i])
print(max(max_cnt))