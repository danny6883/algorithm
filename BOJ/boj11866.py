import collections
n, k = map(int, input().split())
ans = []
deque_x = collections.deque([i for i in range(1,n+1)])
while deque_x:
    deque_x.rotate(1-k)
    ans.append(deque_x.popleft())
print('<' + ', '.join(map(str,ans)) + '>')