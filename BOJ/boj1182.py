N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
for i in range(1,2**N):
    sum = 0
    index = 0
    while i:
        if i%2:
            sum += nums[index]
        i //= 2
        index += 1
    if sum == S:
        cnt += 1
print(cnt)