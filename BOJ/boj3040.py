import itertools
nums = [int(input()) for _ in range(9)]
comb = list(itertools.combinations([i for i in range(9)],2))
sum_nums = sum(nums)
for first, second in comb:
    if sum_nums - nums[first] - nums[second] == 100:
        for i in range(9):
            if i != first and i != second:
                print(nums[i])
        break