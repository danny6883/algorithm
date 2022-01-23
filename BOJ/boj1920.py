n = int(input())
an = list(map(int, input().split()))
an.sort()
m = int(input())
am = list(map(int, input().split()))
ans = []

def search(num, start, end):
    if start > end:
        return '0'
    index = (start + end) // 2
    if an[index] < num:
        return search(num, index+1, end)
    elif an[index] > num:
        return search(num, start, index-1)
    else:
        return '1'

for ami in am:
    ans.append(search(ami,0,n-1))
print('\n'.join(ans))