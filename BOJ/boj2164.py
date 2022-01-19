import collections
n = int(input())
deque_x = collections.deque([i for i in range(1,n+1)])
while len(deque_x) > 1:
    deque_x.popleft()
    deque_x.append(deque_x.popleft())
print(deque_x.pop())