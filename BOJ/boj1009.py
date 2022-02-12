T = int(input())
ans = []
for _ in range(T):
    a, b = map(int, input().split())
    temp = a%10
    if temp == 0:
        temp = 10
    memory = [temp]
    for i in range(b-1):
        temp = temp * a % 10
        if temp == 0:
            temp = 10
        if temp not in memory:
            memory.append(temp)
        else:
            break
    ans.append(str(memory[(b-1)%len(memory)]))
print('\n'.join(ans))