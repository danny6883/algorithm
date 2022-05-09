N = int(input())
AN = list(map(int, input().split()))
temp_sum = 0
sum_AN = [0]
for k in range(N):
    temp_sum += AN[k]
    sum_AN.append(temp_sum)
M = int(input())
ans = []
for _ in range(M):
    i, j = map(int, input().split())
    ans.append(str(sum_AN[j] - sum_AN[i-1]))
print('\n'.join(ans))