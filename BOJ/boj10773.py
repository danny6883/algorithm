import sys
read = sys.stdin.readline

stack = []
for _ in range(int(read())):
    temp = int(read())
    if temp:
        stack.append(temp)
    else:
        stack.pop()
print(sum(stack))