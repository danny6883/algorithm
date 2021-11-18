alpha = [0]*26
for _ in range(int(input())):
    word = input()
    for i in range(len(word)):
        alpha[ord(word[-i-1])-ord('A')] += 10**i
alpha.sort(reverse=True)
result = 0
for i in range(len(alpha)):
    result += (9-i)*alpha[i]
print(result)