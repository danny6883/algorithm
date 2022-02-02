import sys, heapq
read = sys.stdin.readline

ans = []
for _ in range(int(read())):
    nums = dict()
    min_heap = []
    max_heap = []
    Q = int(read())
    for i in range(Q):
        operation, n = read().split()
        n = int(n)
        if operation == 'I':
            heapq.heappush(min_heap,n)
            heapq.heappush(max_heap,-n)
            if n in nums:
                nums[n] += 1
            else:
                nums[n] = 1
        else:
            if n == 1:
                if nums:
                    del_n = -heapq.heappop(max_heap)
                    while del_n not in nums:
                        del_n = -heapq.heappop(max_heap)
                    if nums[del_n] > 1:
                        nums[del_n] -= 1
                    else:
                        nums.pop(del_n)
            else:
                if nums:
                    del_n = heapq.heappop(min_heap)
                    while del_n not in nums:
                        del_n = heapq.heappop(min_heap)
                    if nums[del_n] > 1:
                        nums[del_n] -= 1
                    else:
                        nums.pop(del_n)
    if nums:
        max_n = -heapq.heappop(max_heap)
        while max_n not in nums:
            max_n = -heapq.heappop(max_heap)
        min_n = heapq.heappop(min_heap)
        while min_n not in nums:
            min_n = heapq.heappop(min_heap)
        ans.append(str(max_n)+' '+str(min_n))
    else:
        ans.append('EMPTY')
print('\n'.join(ans))