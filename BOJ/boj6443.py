import sys
read = sys.stdin.readline

def bt(alpha,w):
    if len(w) == len_word:
        anagram.append(w)
        return
    for i in range(26):
        if alpha[i]:
            alpha[i] -= 1
            bt(alpha,w+chr(i + ord('a')))
            alpha[i] += 1

ans = []
N = int(read())
for _ in range(N):
    word = read().rstrip()
    alpha = [0]*26
    anagram = []
    for i in range(len(word)):
        alpha[ord(word[i]) - ord('a')] += 1

    len_word = len(word)
    bt(alpha,'')
    ans += anagram
print('\n'.join(ans))