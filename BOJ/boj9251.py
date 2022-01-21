first = input()
second = input()

LCS = [0 for _ in range(len(second))]
for s1 in range(len(first)):
    temp = 0
    for s2 in range(len(second)):
        if temp < LCS[s2]:
            temp = LCS[s2]
        elif first[s1] == second[s2]:
            LCS[s2] = temp + 1
print(max(LCS))