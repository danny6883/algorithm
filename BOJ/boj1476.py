E, S, M = map(int, input().split())
E %= 15
M %= 19
for i in range(286):
    temp = S + i*28
    if temp % 15 == E and temp % 19 == M:
        break
print(temp)