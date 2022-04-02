S = input()
alpha = [0]*26
for character in S:
    alpha[ord(character)-ord('a')] += 1
print(' '.join(map(str,alpha)))