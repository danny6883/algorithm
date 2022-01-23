import sys
read = sys.stdin.readline

n, c = map(int, read().split())
houses = [int(read()) for _ in range(n)]
houses.sort()
left = 1
right = 10**9

def install(length):
    last = 0
    count = 1
    next = houses[last] + length
    while next <= houses[-1]:
        while houses[last] < next:
            last += 1
        count += 1
        next = houses[last] + length
    return count

while left <= right:
    mid = (left + right) // 2
    count = install(mid)
    if count < c:
        right = mid - 1
    else:
        left = mid + 1
        ans = mid
print(ans)