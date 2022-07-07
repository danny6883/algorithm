N, M = map(int, input().split())
nums = list(set(map(int, input().split())))
nums.sort()

ans = [[n] for n in nums]
for _ in range(M-1):
    temp = []
    for arr in ans:
        i = 0
        while nums[i] < arr[-1]:
            i += 1
        while i < N:
            temp.append(arr+[nums[i]])
            i += 1
    ans = temp[:]
for arr in ans:
    print(*arr)